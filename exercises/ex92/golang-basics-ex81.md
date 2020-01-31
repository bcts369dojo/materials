# Go Basics 演習 81 goroutine

次のコードを実行結果はどうなりますか？

ヒント: チャンネルへのデータ送信について理解しましょう。

<https://play.golang.org/p/oq2xm1e0R83> で動作確認できます。

```go
// bcts369道場 Go Basics 演習81 goroutine
package main

import (
	"fmt"
)

func main() {
	c := make(chan int)
	go func() {
		c <- 1
	}()
	fmt.Println(<-c)
}
```
