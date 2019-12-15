# Go Basics 演習 74 interface

次のコードを実行すると、どのように表示されますか？

ヒント: この演習ではポリモーフィズム（多態性）を使用しています。多態性とは、型の実装を通じてさまざまな動作を行うことができるコードを作成する機能です。

https://play.golang.org/p/fNC3q3uWgys で動作確認できます。

```go
// bcts369道場 Go Basics 演習74 interface
package main

import (
	"fmt"
	"math"
)

// 正方形
type square struct {
	side float64
}

// 丸
type circle struct {
	radius float64
}

// 形状という型を表現するインターフェース
type shape interface {
	area() float64 // 面積を返します
}

// interfaceを実装します（正方形）
func (s square) area() float64 {
	return s.side * s.side
}

// interfaceを実装します（丸）
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

// 形状という型を引き数として受け取る関数
func info(z shape) {
	fmt.Println(z)
	fmt.Println(z.area())
}

func main() {
	s := square{10}
	c := circle{5}
	info(s) // 正方形の面積
	info(c) // 円の面積
}
```
