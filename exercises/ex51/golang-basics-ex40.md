# Go Basics 演習 40 array

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/Et8nfkkZTZk 動作確認できます。

```go
// bcts369道場 Go Basics 演習40 array
package main

import "fmt"

func main() {
	var x [10]int
	fmt.Println(x)
	fmt.Println(len(x))
	fmt.Println(x[2])
	x[2] = 777
	fmt.Println(x[2])
	fmt.Println(x)
}
```
