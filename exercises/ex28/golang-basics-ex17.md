# Go Basics 演習17 ポインター

次のコードを実行すると、 `fmt.Println(a)` の結果はどのように表示されますか？

https://play.golang.org/p/XIRl3ZIjn-6 で動作確認できます。


```go
package main

import "fmt"

func main() {
	a := 10

	fmt.Println(a)  // 10
	fmt.Println(&a) // aのアドレスが表示されます

	var b = &a      // bにaのアドレスを格納します
	fmt.Println(b)  // bに格納されたaのアドレスが表示されます
	fmt.Println(*b) // bに格納されたaのアドレスの中身（値）が表示されます

	*b = 20        // bのアドレスの中身（値）を変更します
	fmt.Println(a) // <--- 何が表示されますか？
}
```
