# Go Basics 演習 47 slice

次のコードを実行すると、どのように表示されますか？

ヒント: 可変長配列に要素を追加する例です。

https://play.golang.org/p/bOgpomRJEkl 動作確認できます。

```go
package main

import "fmt"

func main() {
        mySlice1 := []string{"1", "2"}
        mySlice2 := []string{"3", "4", "5"}

        mySlice1 = append(mySlice1, mySlice2...)
        fmt.Println(mySlice1)

        mySlice1 = append(mySlice1[:2], mySlice1[3:]...)
        fmt.Println(mySlice1)
}
```
