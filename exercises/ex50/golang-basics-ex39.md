# Go Basics 演習 39 Function

次のコードを実行すると、どのように表示されますか？

ヒント： 無名関数を即時実行する場合はどうしたらよいですか？

https://play.golang.org/p/DMrVgaMELW_E で動作確認できます。

```go
// bcts369道場 Go Basics 演習39 Function
package main

import "fmt"

func main() {
	func() {
		fmt.Println("無名関数が実行されました")
	}()
}
```
