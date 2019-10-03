# Go Basics 演習16 ポインター

次のコードを実行すると、 `fmt.Println(*b)` の結果はどのように表示されますか？

https://play.golang.org/p/ux1j9p6g0XH で動作確認できます。


```go
package main

import "fmt"

func main() {

	a := 10
	fmt.Printf("%T\n", a) // a は int型であることがわかります
	fmt.Println(a)        // 10と表示されます
	fmt.Println(&a)       // a のアドレスが表示されます

	var b = &a            // a のアドレスが `b` に格納されます
	fmt.Printf("%T\n", b) // b は intのポインター型であることがわかります
	fmt.Println(b)        // b に格納されている値（アドレス）を表示されます
	fmt.Println(*b)       // 何が表示されますか？
}
```
