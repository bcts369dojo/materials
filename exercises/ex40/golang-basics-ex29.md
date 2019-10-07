# Go Basics 演習 29 if 文

次のコードを実行すると、どのように表示されますか？

ヒント： ありません

https://play.golang.org/p/NWpWgsxgnz5 で動作確認できます。

```go
package main

import "fmt"

func mod2(num int) string {
	if num%2 == 0 {

		return "ok"
	} else {
		return "no"
	}
}

func main() {
	if result := mod2(10); result == "ok" {
		fmt.Println("OK")
	}
	// fmt.Println(result) // これはエラーになる

	num := 10
	if num%2 == 0 {
		fmt.Println("num % 2:", num%2)
	} else if num%3 == 0 {
		fmt.Println("num % 3:", num%3)

	} else {
		fmt.Println("else")
	}
}
```
