package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z int = int(f)
	fmt.Println(x, y, z)

	i := 42
	j := float64(i)
	k := uint(j)
	fmt.Println(i, j, k)
}
