# Go Basics 演習11  スコープ

次のコードを実行すると、 何が表示されますか？ 

https://play.golang.org/p/5yTlpQS5EZ3 で動作確認できます。

ヒント： 変数 increment の型とスコープに注目してください

```go
// bcts369道場 Go Basics 演習11 スコープ
// 何が表示されますか？

package main

import "fmt"

func wrapper() (func() int) {
	x := 0
	return func() int {
		x++
		return x
	}
}

func main() {
	increment := wrapper()
	fmt.Printf("%T\n", increment)
	
	fmt.Println(increment())
	fmt.Println(increment())
	
	increment = wrapper()	
	fmt.Println(increment())
}

```

