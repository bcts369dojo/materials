# Go Basics 演習 44 slice

次のコードを実行すると、どのように表示されますか？

ヒント: ２つの for 文による違いに注目してください。

https://play.golang.org/p/K8gt92W-N99 動作確認できます。

```go
// bcts369道場 Go Basics 演習44 slice
package main

import "fmt"

func main() {

	items := []string{
		"item1",
		"item2",
		"item3",
	}

	for i, currentEntry := range items {
		fmt.Println(i, currentEntry)
	}

	for j := 0; j < len(items); j++ {
		fmt.Println(items[j])
	}

}
```
