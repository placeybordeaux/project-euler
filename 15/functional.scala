object problem15 {
    val cache = collection.mutable.HashMap[(Int,Int),Long]()

    def problem15(x: Int, y: Int): Long = {
        if (!cache.contains((x,y))) {
            cache((x,y)) = {
                (x,y) match {
                    case (_ , 0) => 1.toLong
                    case (0, _) => 1.toLong
                    case (x, y) => problem15(x-1,y) + problem15(x,y-1)
                }
            }
        }
	println((x,y))
        cache((x,y))
    }
    
    def main(args: Array[String]) {
        println(problem15(20,20))
    }
}
