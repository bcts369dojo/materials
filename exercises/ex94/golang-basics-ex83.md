# Go Basics 演習 83 goroutine

次のコードの実行結果はどうなりますか？

ヒント: 値が入ったチャンネルを返す関数とclose()を使う場所についてググっておくとよいでしょう。

<https://play.golang.org/p/I6aJod1nIu6> で動作確認できます。

```go
// bcts369道場 Go Basics 演習83 goroutine
package main

import (
	"fmt"
)

func main() {
	c := factorial(4)
	for n := range c {
		fmt.Println(n)
	}
}

func factorial(n int) chan int {
	out := make(chan int)
	go func() {
		total := 1
		for i := n; i > 0; i-- {
			total *= i
		}
		out <- total
		close(out)
	}()
	return out
}
```
