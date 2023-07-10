package cse512

import java.sql.Timestamp
import java.text.SimpleDateFormat
import java.util.Calendar

object HotcellUtils {
  val coordinateStep = 0.01

  def CalculateCoordinate(inputString: String, coordinateOffset: Int): Int =
  {
    // Configuration variable:
    // Coordinate step is the size of each cell on x and y
    var result = 0
    coordinateOffset match
    {
      case 0 => result = Math.floor((inputString.split(",")(0).replace("(","").toDouble/coordinateStep)).toInt
      case 1 => result = Math.floor(inputString.split(",")(1).replace(")","").toDouble/coordinateStep).toInt
      // We only consider the data from 2009 to 2012 inclusively, 4 years in total. Week 0 Day 0 is 2009-01-01
      case 2 => {
        val timestamp = HotcellUtils.timestampParser(inputString)
        result = HotcellUtils.dayOfMonth(timestamp) // Assume every month has 31 days
      }
    }
    return result
  }

  def timestampParser (timestampString: String): Timestamp =
  {
    val dateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss")
    val parsedDate = dateFormat.parse(timestampString)
    val timeStamp = new Timestamp(parsedDate.getTime)
    return timeStamp
  }

  def dayOfYear (timestamp: Timestamp): Int =
  {
    val calendar = Calendar.getInstance
    calendar.setTimeInMillis(timestamp.getTime)
    return calendar.get(Calendar.DAY_OF_YEAR)
  }

  def dayOfMonth (timestamp: Timestamp): Int =
  {
    val calendar = Calendar.getInstance
    calendar.setTimeInMillis(timestamp.getTime)
    return calendar.get(Calendar.DAY_OF_MONTH)
  }

  def calculateModifiedScore(pickupPoints: Int, numNeighbors: Int, numCells: Int, average: Double, standardDeviation: Double): Double = {
    val numerator = pickupPoints.toDouble - (average * numNeighbors.toDouble)
    val denominator = standardDeviation * math.sqrt(((numCells.toDouble * numNeighbors.toDouble) - math.pow(numNeighbors.toDouble, 2)) / (numCells.toDouble - 1.0))
    val result = numerator / denominator

    result
  }

  def calculateNumNeighbors(xInput: Int, yInput: Int, zInput: Int, xMin: Int, yMin: Int, zMin: Int, xMax: Int, yMax: Int, zMax: Int): Int = {
    var neighborCheck = 0
    var totalNeighbors = 26
    var missingNeighbors = 0
    
    if (xInput == xMin || xInput == xMax) {
      neighborCheck += 1
    }
    if (yInput == yMin || yInput == yMax) {
      neighborCheck += 1
    }
    if (zInput == zMin || zInput == zMax) {
      neighborCheck += 1
    }

    missingNeighbors = neighborCheck match {
      case 0 => 0
      case 1 => 9
      case 2 => 15
      case 3 => 19
    }
    
    totalNeighbors - missingNeighbors
  }

}
