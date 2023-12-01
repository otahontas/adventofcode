object Main extends App {
  val file = "input.txt"
  val lines = scala.io.Source.fromFile(file).getLines.toList

  // First
  val digitRegex = "\\d".r
  println(
    lines
      .map(line => {
        val l = digitRegex.findAllIn(line).toList
        val a = l.head
        val b = l.last
        s"$a$b".toInt
      })
      .sum
  )

  // Second
  val nameToNum = Map(
    "zero" -> 0,
    "one" -> 1,
    "two" -> 2,
    "three" -> 3,
    "four" -> 4,
    "five" -> 5,
    "six" -> 6,
    "seven" -> 7,
    "eight" -> 8,
    "nine" -> 9
  )
  val nameToNumKeys = nameToNum.keys.mkString("|")
  val digitNameRegex = s"(?=(\\d|$nameToNumKeys))".r
  println(
    lines
      .map(line => {
        val l = digitNameRegex.findAllMatchIn(line).map(_.group(1)).toList
        val a = l.head match {
          case digitRegex() => l.head.toInt
          case _            => nameToNum(l.head)
        }
        val b = l.last match {
          case digitRegex() => l.last.toInt
          case _            => nameToNum(l.last)
        }
        s"$a$b".toInt
      })
      .sum
  )
}
