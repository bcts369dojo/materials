# Go Basics 演習21 forループ

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/z7B88t3KjAF で動作確認できます。


```go
package main

import "fmt"

func main() {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			fmt.Println(i, " - ", j)
		}
	}
}
```
