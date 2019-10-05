# Go Basics 演習25 Switch文

次のコードを実行すると、どのように表示されますか？

ヒント: インターフェース型の変数には、いろんな型を導入できますが、   switch 文で簡単に判別できます。

https://play.golang.org/p/WF07QYhBQ-J で動作確認できます。


```go
package main

import "fmt"

type dog struct {
	name string
	age  int
}

// 引数 x はインターフェースなので、あらゆる型を指定できますが、どのような型か判断する必要があります。
func SwitchOnType(x interface{}) {
	switch x.(type) { // xのタイプを判断します
	case int:
		fmt.Println("int")
	case string:
		fmt.Println("string")
	case dog:
		fmt.Println("dog info")
	default:
		fmt.Println("unknown")

	}
}

func main() {
	SwitchOnType(1)
	SwitchOnType("Hello")
	var t = dog{"Siro", 5}
	SwitchOnType(t)
	SwitchOnType(t.name)
	SwitchOnType(1.1)
}
```
