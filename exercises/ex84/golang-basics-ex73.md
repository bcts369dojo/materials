# Go Basics 演習 73 interface

次のコードを実行すると、どのように表示されますか？

ヒント: 定義した interface は新たな型として使うことができ、interface で定義された関数を実装した構造体を、この型として代入することができます。

https://play.golang.org/p/P6AsLepXxyP で動作確認できます。

```go
// bcts369道場 Go Basics 演習73 interface
package main

import "fmt"

type square struct {
	side float64
}

// interfaceを実装
func (z square) area() float64 {
	return z.side * z.side
}

type shape interface {
	area() float64
}

func info(z shape) {
	fmt.Println(z)
	fmt.Println(z.area())
	fmt.Printf("%T\n", z.area())
}

func main() {
	s := square{10}
	fmt.Printf("%T\n", s)
	info(s) // shape型のレシーバにsquare型を渡しているがエラーにならないのはなぜ？
}
```
