# Go Basics 演習14  定数 

次のコードを実行すると、 どのように表示されますか？ 

https://play.golang.org/p/z_monl7nzeI で動作確認できます。

```go
package main

import "fmt"

const (
	_ = iota
	b = iota * 10
	c = iota * 10
)

func main() {
	fmt.Println(b)
	fmt.Println(c)
}
```

