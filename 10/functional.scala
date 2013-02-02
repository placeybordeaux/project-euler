import scala.math._

def seive(end: Long):Array[Long] = {
   var primes: Array[Long] = (0 to end.toInt).map(_.toLong).toArray;
   for (i <- 2 until scala.math.sqrt(end).toInt if primes(i) > 0) {
        for (j <- (i + i) until end.toInt + 1 by i) {
          primes(j) = 0
        }
    }
    primes.filter(e => 1 < e)
  }
val primes = seive(2000000)
println(primes.reduceLeft(_+_))
