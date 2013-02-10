object euler23 {
  def main(args: Array[String]) {
    val t1 = System.currentTimeMillis()
    val abundants = List.range(1,28123).filter(abundant)
    var sum = 0
    for(i <- 1 to 28123){
      val SubtractedAbundants = abundants.map(i-_)
      if(SubtractedAbundants.intersect(abundants).size == 0){
        sum += i
      }
    }
    println(sum)
    println(System.currentTimeMillis() - t1)
  }

  def abundant(n: Int): Boolean = {
    return (divisors(n).sum > n)
  }

  def divisors(n: Int): collection.mutable.Set[Int] = {
    val set = collection.mutable.Set(1)
    for(i <- 2 until n)
      {
        if(n%i == 0)
          {
            set += i
          }
      }
    return set
  }
}

