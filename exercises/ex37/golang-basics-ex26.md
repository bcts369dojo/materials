# Go Basics 演習26 if文

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/JE-TxHbBjmB で動作確認できます。

```go
package main

import "fmt"

func main() {

	b := true

	if food := "ramen"; b {
		fmt.Println(food)
	}
}
```
