# Go Basics 演習 84 エラーハンドリング

このコードは正しく動作しますが、改善すべき点があります。どのように書き換えるべきでしょうか？

ヒント: 早期リターンという観点から考えてみてください。


<https://play.golang.org/p/s9t3yajnQuk> で動作確認できます。

```go
// bcts369道場 Go Basics 演習84 エラーハンドリング

package main

import "fmt"

func main() {
	x := 10
	str := evalInt(x)
	fmt.Println(str)
}

func evalInt(n int) string {
	if n > 10 {
		return fmt.Sprint("xは10より大きい")
	} else { // この判定は必要？
		return fmt.Sprint("xは10以下")
	}
}
```
