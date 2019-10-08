# Go Basics 演習 31 Function

次のコードを実行すると、どのように表示されますか？

ヒント： ありません

https://play.golang.org/p/lEAJGKeMMnj で動作確認できます。

```go
// bcts369道場 Go Basics 演習31 Function
package main

import "fmt"

func main() {
	fmt.Println(greet("Taro ", "Yamada "))
}

func greet(fname, lname string) string {
	return fmt.Sprint(fname, lname)
}
```
