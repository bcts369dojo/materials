# Go Basics 演習 78 goroutine

次のコードを実行すると、実は何も表示されません。なぜでしょうか？

ヒント: この例は一般的です。まずはググってみてください。

https://play.golang.org/p/f4wp85zEYPg で動作確認できます。

```go
// bcts369道場 Go Basics 演習78 goroutine
package main

import "fmt"

func foo() {
	for i := 0; i < 10; i++ {
		fmt.Println("Foo:", i)
	}
}

func bar() {
	for i := 0; i < 10; i++ {
		fmt.Println("Bar:", i)
	}
}

func main() {
	go foo()
	go bar()
}
```
