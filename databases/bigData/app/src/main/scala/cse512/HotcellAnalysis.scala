package cse512

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.sql.functions.udf
import org.apache.spark.sql.functions._

object HotcellAnalysis {
  Logger.getLogger("org.spark_project").setLevel(Level.WARN)
  Logger.getLogger("org.apache").setLevel(Level.WARN)
  Logger.getLogger("akka").setLevel(Level.WARN)
  Logger.getLogger("com").setLevel(Level.WARN)

def runHotcellAnalysis(spark: SparkSession, pointPath: String): DataFrame =
{
  // Load the original data from a data source
  var pickupInfo = spark.read.format("com.databricks.spark.csv").option("delimiter",";").option("header","false").load(pointPath);
  pickupInfo.createOrReplaceTempView("nyctaxitrips")
  pickupInfo.show()

  // Assign cell coordinates based on pickup points
  spark.udf.register("CalculateX",(pickupPoint: String)=>((
    HotcellUtils.CalculateCoordinate(pickupPoint, 0)
    )))
  spark.udf.register("CalculateY",(pickupPoint: String)=>((
    HotcellUtils.CalculateCoordinate(pickupPoint, 1)
    )))
  spark.udf.register("CalculateZ",(pickupTime: String)=>((
    HotcellUtils.CalculateCoordinate(pickupTime, 2)
    )))
  pickupInfo = spark.sql("select CalculateX(nyctaxitrips._c5),CalculateY(nyctaxitrips._c5), CalculateZ(nyctaxitrips._c1) from nyctaxitrips")
  var newCoordinateName = Seq("x", "y", "z")
  pickupInfo = pickupInfo.toDF(newCoordinateName:_*)
  pickupInfo.show()

  // Define the min and max of x, y, z
  val minX = -74.50/HotcellUtils.coordinateStep
  val maxX = -73.70/HotcellUtils.coordinateStep
  val minY = 40.50/HotcellUtils.coordinateStep
  val maxY = 40.90/HotcellUtils.coordinateStep
  val minZ = 1
  val maxZ = 31
  val numCells = (maxX - minX + 1)*(maxY - minY + 1)*(maxZ - minZ + 1)

  pickupInfo.createOrReplaceTempView("pickupInfo")


  //Selecting the hot cells and their counts(of pickups)
  val query = s"select x, y, z, count(*) as pickupCount from pickupInfo where x >= $minX and x <= $maxX and y >= $minY and y <= $maxY and z >= $minZ and z <= $maxZ group by z, y, x"
  var hotCellPoints = spark.sql(query)
  hotCellPoints.createOrReplaceTempView("hotCellPoints")

  // Computing Sum of Xj and XjSquare from hotCellPoints
  val sq_x_j = spark.sql("select sum(pickupCount) as sumOfXj, sum(pickupCount * pickupCount) as sqsumOfXj from hotCellPoints")
  sq_x_j.createOrReplaceTempView("sq_x_j")

  //fetching values for Xj and XjSquare
  val sq_x_jRow = sq_x_j.first()
  val sumOfXj = sq_x_jRow.getAs[Long]("sumOfXj").toDouble
  val sqSumOfXj = sq_x_jRow.getAs[Long]("sqsumOfXj").toDouble

  // Computing mean and S needed for the Getis-Ord Stat score
  val X_mean = sumOfXj / numCells.toDouble
  val S = math.sqrt(sqSumOfXj / numCells.toDouble - X_mean * X_mean)

  // Self join on hotCellPoint to get neighbours of each cell
  spark.udf.register("neighbors", (inputX: Int, inputY: Int, inputZ: Int, minX: Int, minY: Int, minZ: Int, maxX: Int, maxY: Int, maxZ: Int) => HotcellUtils.calculateNumNeighbors(inputX, inputY, inputZ, minX, minY, minZ, maxX, maxY, maxZ))
  val neighborCells = spark.sql(
    s"""SELECT neighbors(hcp1.x, hcp1.y, hcp1.z, $minX, $minY, $minZ, $maxX, $maxY, $maxZ) AS neighborCellCount,
      |hcp1.x AS x, hcp1.y AS y, hcp1.z AS z, SUM(hcp2.pickupCount) AS i_j_x_j
      |FROM hotCellPoints AS hcp1, hotCellPoints AS hcp2
      |WHERE (hcp2.x = hcp1.x-1 OR hcp2.x = hcp1.x OR hcp2.x = hcp1.x+1)
      |AND (hcp2.y = hcp1.y-1 OR hcp2.y = hcp1.y OR hcp2.y = hcp1.y+1)
      |AND (hcp2.z = hcp1.z-1 OR hcp2.z = hcp1.z OR hcp2.z = hcp1.z+1)
      |GROUP BY hcp1.z, hcp1.y, hcp1.x""".stripMargin)
  neighborCells.createOrReplaceTempView("neighborCells")

  spark.udf.register("GetisOrdStat", (i_j_x_j: Int, neighborCellCount: Int, numCells: Int, X_mean: Double, S: Double) => HotcellUtils.calculateModifiedScore(i_j_x_j, neighborCellCount, numCells, X_mean, S))

  val getisOrdStatCells = spark.sql(s"""select GetisOrdStat(i_j_x_j, neighborCellCount, $numCells, $X_mean, $S) as GetisOrdStat, x, y, z from neighborCells order by GetisOrdStat desc""")
  getisOrdStatCells.show()
  getisOrdStatCells.createOrReplaceTempView("GetisOrdStatCells")

  // x,y,z values sorted based on GetisOrdStat score
  val resultInfo = spark.sql("select x, y, z  from GetisOrdStatCells order by GetisOrdStat desc")
  resultInfo.createOrReplaceTempView("finalPickupInfo")

  return resultInfo.coalesce(1)
}
}
