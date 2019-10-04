# Go Basics 演習19 forループ

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/sHYRWW2aEg6 で動作確認できます。


```go
// bcts369道場 Go Basics 演習19 forループ
package main

import "fmt"

func main() {
	i := 0
	for {
		fmt.Println(i)
		if i >= 10 {
			break
		}
		i++
	}
}
```
