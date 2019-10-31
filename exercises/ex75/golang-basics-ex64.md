# Go Basics 演習 64 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 「値型」としてメソッド定義されたものが「値レシーバ」です。 関数定義は func (レシーバ値 レシーバ型) 関数名という形になります。

https://play.golang.org/p/iuBwG-kslTh で動作確認できます。

```go
// bcts369道場 Go Basics 演習64 struct
package main

import "fmt"

type someStruct struct {
	count int
}

// 値レシーバ
func (s someStruct) add() {
	s.count += 1
}

func main() {
	some := someStruct{0}
	some.add()
	fmt.Println(some.count)
}
```
