# Go Basics 演習9  スコープ

次のコードを実行すると、 コンパイルでエラーが発生します。なぜでしょうか？ 

https://play.golang.org/p/EB_Ic11hLXg で動作確認できます。

エラーが発生しないように修正してください。

```go
package main

import "fmt"

func main() {
	x := 100
	fmt.Println(x)
	{
		fmt.Println(x)
		y := "Hello."
		fmt.Println(y)
	}
	fmt.Println(y) // undefined: y
}
```

