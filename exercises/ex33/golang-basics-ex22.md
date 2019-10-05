# Go Basics 演習22 Switch文

次のコードを実行すると、どのように表示されますか？

ヒント： **fallthrough** というキーワードに注目してください

https://play.golang.org/p/mkDzUsO6htj で動作確認できます。


```go
package main

import "fmt"

func main() {
	switch "3" {
	case "1":
		fmt.Println("this is 1")
	case "2":
		fmt.Println("this is 2")
	case "3":
		fmt.Println("this is 3")
		fallthrough
	case "4":
		fmt.Println("this is 4")
		fallthrough
	case "5":
		fmt.Println("this is 5")
	case "6":
		fmt.Println("this is 6")
	}
}
```
