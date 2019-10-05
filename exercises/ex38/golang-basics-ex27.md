# Go Basics 演習27 if文

次のコードを実行すると、エラーが発生します。なぜでしょうか？

ヒント： food変数のスコープに注目してください

https://play.golang.org/p/sbhh2Q52CpQ で動作確認できます。

```go
package main

import "fmt"

func main() {

	b := true

	if food := "ramen"; b {
		fmt.Println(food)
	}

	fmt.Println(food) // undefined エラー
}
```
