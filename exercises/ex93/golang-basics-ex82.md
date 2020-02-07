# Go Basics 演習 82 goroutine

次のコードを実行するとデッドロックを引き起こしエラーが発生します？ なぜでしょうか？ デッドロックを回避するコードを考えてみてください。ちなみに、表示されるエラーメッセージは全てのgoroutineが待ちに入った時に表示されます。

ヒント: デッドロックについてググってみましょう。

<https://play.golang.org/p/vB2FHpntt7t> で動作確認できます。

```go
// bcts369道場 Go Basics 演習82 goroutine
package main

import (
	"fmt"
)

func main() {
	c := make(chan int)
	c <- 1
	fmt.Println(<-c)
}
```
