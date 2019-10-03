# Go Basics 演習13  定数 

次のコードを実行すると、 どのように表示されますか？ 

https://play.golang.org/p/gM9E38-8bzN で動作確認できます。

```go
package main

import "fmt"

const (
	a = iota
	b
	c
)

const (
	d = iota
	e
	f
)

func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
}

```

