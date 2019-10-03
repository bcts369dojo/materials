# Go Basics 演習5  スコープ

次のコードを実行すると、 コンパイルでエラーが発生します。なぜでしょうか？ そして、解決した場合はどのように表示されますか？

https://play.golang.org/p/iE0lLvGvQe_K で動作確認できます。

エラーが発生しないように修正してください。


```go
package main

import "fmt"

func main() {
	x := 42
	fmt.Println(x)
	foo()
}

func foo() {
	fmt.Println(x)
}

```

