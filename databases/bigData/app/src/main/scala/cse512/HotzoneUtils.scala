package cse512

object HotzoneUtils {

  def ST_Contains(queryRectangle: String, pointString: String ): Boolean = {
    val rectangleCoords = queryRectangle.split(",").map(_.toDouble)
    val pointCoords = pointString.split(",").map(_.toDouble)

    val minX = Math.min(rectangleCoords(0), rectangleCoords(2))
    val minY = Math.min(rectangleCoords(1), rectangleCoords(3))
    val maxX = Math.max(rectangleCoords(0), rectangleCoords(2))
    val maxY = Math.max(rectangleCoords(1), rectangleCoords(3))

    val pointX = pointCoords(0)
    val pointY = pointCoords(1)

    return pointX >= minX && pointX <= maxX && pointY >= minY && pointY <= maxY
  }
}
