# Go Basics 演習 36 Function

次のコードを実行すると、どのように表示されますか？

ヒント： factrial 関数の中で factorial 関数が呼ばれています。これは **再帰** というテクニックです。覚えておきましょう。

https://play.golang.org/p/id8-fePkkeW で動作確認できます。

```go
package main

import "fmt"

func factorial(x int) int {
	if x == 0 {
		return 1
	}
	return x * factorial(x-1)
}

func main() {
	fmt.Println(factorial(4))
}
```
