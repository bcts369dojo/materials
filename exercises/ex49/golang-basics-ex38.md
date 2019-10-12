# Go Basics 演習 38 Function

次のコードを実行すると、どのように表示されますか？

ヒント：`defer` は関数を抜ける直前に実行されます。1 つの関数内に複数の `defer` が存在する場合は、最後に追加された`defer`から、最初に追加された`defer`の順番で実行されます。なお、`defer`はいくつでも追加できます。

https://play.golang.org/p/1Rv1Ln88aVw で動作確認できます。

```go
// bcts369道場 Go Basics 演習38 Function
package main

import "fmt"

func func1() {
	fmt.Println("func1")
}

func func2() {
	fmt.Println("func2")
}

func func3() {
	fmt.Println("func3")
}

func main() {
	fmt.Println("1")
	defer func1()
	fmt.Println("2")
	defer func2()
	func3()
	fmt.Println("3")
}
```
