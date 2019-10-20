# Go Basics 演習 47 slice 

次のコードを実行すると、どのように表示されますか？

ヒント: 可変長配列に要素を追加する例です。 

https://play.golang.org/p/lvqP_A-vpp1 動作確認できます。


```go
// bcts369道場 Go Basics 演習47 slice
package main

import "fmt"

func main() {

        intSlice1 := []int{1, 2, 3, 4, 5}
        intSlice2 := []int{6, 7, 8, 9}

        intSlice1 = append(intSlice1, intSlice2...)

        fmt.Println(intSlice1)
}
```
