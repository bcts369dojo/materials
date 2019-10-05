# Go Basics 演習22 Switch文

次のコードを実行すると、どのように表示されますか？


https://play.golang.org/p/Qsu9Zy4bOsz で動作確認できます。


```go
package main

import "fmt"

func main() {
	switch "6" {
	case "0", "1":
		fmt.Println("0 or 1")
	case "2", "3":
		fmt.Println("2 or 3")
	case "4", "5", "6":
		fmt.Println("4 or 5 or 6")
	}
}
```
