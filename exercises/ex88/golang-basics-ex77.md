# Go Basics 演習 77 interface

次のコードを実行すると、どのように表示されますか？

ヒント: 型の変換方法についてググっておきましょう。

https://play.golang.org/p/omxjce1aMhI で動作確認できます。

```go
// bcts369道場 Go Basics 演習77 interface
package main

import "fmt"

func main() {
	b := []byte("hello") // string型を []bytesに変換します。
	fmt.Printf("%T %v\n", b, b)
}
```
