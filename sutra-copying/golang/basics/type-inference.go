package main

import (
	"fmt"
)

func main() {
	v := 42
	fmt.Printf("v is of type %T\n", v)

	f := 3.142
	g := 0.867 + 0.5i
	fmt.Printf("f is of type %T\n", f)
	fmt.Printf("g is of type %T\n", g)
}
