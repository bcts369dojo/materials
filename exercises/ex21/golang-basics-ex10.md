# Go Basics 演習10  スコープ

次のコードを実行すると、 何が表示されますか？ 

https://play.golang.org/p/SfaUSt7R6im で動作確認できます。

ヒント：　変数 x のスコープに注目してください

```go
// bcts369道場 Go Basics 演習10 スコープ
// 何が表示されますか？
package main

import "fmt"

var x = 0

func increment() int {
	x++
	return x
}

func main() {
	fmt.Println(increment())
	fmt.Println(increment())
}
```

