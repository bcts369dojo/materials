# Go Basics 演習20 forループ

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/jFpcP7Ia4NN で動作確認できます。


```go
package main

import "fmt"

func main() {
	i := 0
	for {
		i++
		if i%2 == 0 {
			continue
		}
		fmt.Println(i)
		if i >= 10 {
			break
		}
	}
}
```
