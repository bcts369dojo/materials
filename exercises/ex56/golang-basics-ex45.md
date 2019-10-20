# Go Basics 演習 45 Slice 

次のコードを実行すると、どのように表示されますか？

ヒント:これまでも似たような演習を出しましたが、重要なので動きを理解しておくようにしてください。 

https://play.golang.org/p/M9ksdBSjXps 動作確認できます。

```go
// bcts369道場 Go Basics 演習45 slice
package main

import "fmt"

func main() {
        var results []int
        fmt.Println(results)

        mySlice := []string{"a", "b", "c", "d", "e", "f"}
        fmt.Println(mySlice)
        fmt.Println(mySlice[2:4])
        fmt.Println(mySlice[2])
        fmt.Println(mySlice[2:])
}
```
