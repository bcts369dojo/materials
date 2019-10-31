# Go Basics 演習 65 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 「ポインタ型」としてメソッド定義されたものが「ポインタレシーバ」です。 関数定義は func (レシーバ値 レシーバ型) 関数名という形になります。

https://play.golang.org/p/kpBD28gnOFw で動作確認できます。

```go
// bcts369道場 Go Basics 演習65 struct
package main

import "fmt"

type someStruct struct {
	count int
}

// ポインタレシーバ
func (s *someStruct) add() {
	s.count += 1
}

func main() {
	some := someStruct{0}
	some.add()
	fmt.Println(some.count)
}
```
