# Go Basics 演習 34 Function

次のコードを実行すると、どのように表示されますか？

ヒント：makeGreeter()は文字列を返す関数を返します。

https://play.golang.org/p/Hgb3gDa4jz2 で動作確認できます。

```go
package main

import "fmt"

func makeGreeter() func() string {
	return func() string {
		return "Hello world!"
	}
}

func main() {
	greet := makeGreeter()
	fmt.Printf("%T\n", greet)
	fmt.Println(greet())
}
```
