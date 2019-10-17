# Go Basics 演習 42 slice

次のコードを実行すると、どのように表示されますか？

ヒント: range キーワードに注目してください。

https://play.golang.org/p/YzXJ2tO9ZQX 動作確認できます。

```go
// bcts369道場 Go Basics 演習42 array
package main

import "fmt"

func main() {

	xs := []int{1, 3, 5, 7, 9, 11}

	for i, value := range xs {
		fmt.Println(i, " - ", value)
	}
}
```
