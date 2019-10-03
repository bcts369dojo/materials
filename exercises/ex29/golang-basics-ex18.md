# Go Basics 演習18 ポインター

次のコードでは、 変数xの値を5から0に変更できません。 なぜでしょうか？ 正しく動作するように変更してください。

https://play.golang.org/p/gqg5lSwYarC で動作確認できます。


```go
package main

import "fmt"

func zero(z int) {
	fmt.Printf("%p\n", &z) // 関数zero内でのアドレス
	fmt.Println(z)         // zの中身
	z = 0
}

func main() {
	x := 5
	fmt.Println(x)         // xの値
	fmt.Printf("%p\n", &x) // メイン関数でのアドレス
	fmt.Println(&x)        // メイン関数でのアドレス
	zero(x)                // 変数xの値を0にしたい
	fmt.Println(x)         // xは５のまま
}
```
