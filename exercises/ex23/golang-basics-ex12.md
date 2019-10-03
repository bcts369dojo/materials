# Go Basics 演習12  定数 

次のコードを実行すると、 どのように表示されますか？ 

https://play.golang.org/p/F9E1lZOQ-n9 で動作確認できます。

```go
package main

import "fmt"

const (
	a = iota
	b
	c
)

func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
```

