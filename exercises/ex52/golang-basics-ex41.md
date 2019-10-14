# Go Basics 演習 41 array

次のコードを実行すると、どのように表示されますか？

ヒント: range キーワードに注目してください。

https://play.golang.org/p/n_FRBHSxEwY 動作確認できます。

```go
package main

import "fmt"

func main() {
	var x [10]int

	fmt.Println(len(x))
	fmt.Println(x[9])

	for i := 0; i < 10; i++ {
		x[i] = i
	}
	for i, v := range x {
		fmt.Printf("%v - %T\n", v, v)
		if i > 10 {
			break
		}
	}
}
```
