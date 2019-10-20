# Go Basics 演習 46 slice 

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/Ma_X8QDHYae 動作確認できます。

```go
// bcts369道場 Go Basics 演習46 slice
package main

import "fmt"

func main() {

	strings := make([]string, 3, 5)

	strings[0] = "111"
	strings[1] = "222"
	strings[2] = "333"
	strings = append(strings, "444")
	strings = append(strings, "555")
	strings = append(strings, "666")
	strings = append(strings, "777")

	fmt.Println(strings[6])
	fmt.Println(len(strings))
	fmt.Println(cap(strings))
}
```
