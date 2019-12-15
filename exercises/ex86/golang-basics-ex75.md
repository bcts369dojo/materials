# Go Basics 演習 75 interface

次のコードを実行すると、どのように表示されますか？

ヒント: この演習では演習 74 と同じくポリモーフィズム（多態性）を使用しています。今回は、簡単な応用例として interface 型の可変長引数を受け取る関数を追加しています。 可変長引数は過去の演習で扱っていますが、忘れてしまった方はググるなどして調べてください。

https://play.golang.org/p/tymrFGLGH0K で動作確認できます。

```go
// bcts369道場 Go Basics 演習75 interface
package main

import (
        "fmt"
        "math"
)

type circle struct {
        radius float64
}

type square struct {
        side float64
}

type shape interface {
        area() float64
}

func (c circle) area() float64 {
        return math.Pi * c.radius * c.radius
}

func (s square) area() float64 {
        return s.side * s.side
}

func info(z shape) {
        fmt.Println(z)
        fmt.Println(z.area())
}

// Shape型の可変長引数をとる関数
func totalArea(shapes ...shape) float64 {
        var area float64
        for _, s := range shapes {
                area += s.area()
        }
        return area
}

func main() {
        s := square{10}
        c := circle{5}
        info(s)
        info(c)
        fmt.Println("Total Area: ", totalArea(c, s))
}

```
