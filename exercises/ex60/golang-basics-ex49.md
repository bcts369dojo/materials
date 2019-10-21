# Go Basics 演習 49 slice

次のコードを実行すると、どのように表示されますか？

ヒント: 空のSliceの宣言方法の違いと挙動に注意しましょう。

https://play.golang.org/p/v6rjgjma0qx で動作確認できます。

```go
package main

import (
        "fmt"
)

func main() {
        item1 := []string{}
        items1 := [][]string{}
        fmt.Println(item1)
        fmt.Println(items1)
        fmt.Println(item1 == nil)

        var item2 []string
        var items2 [][]string
        fmt.Println(item2)
        fmt.Println(items2)
        fmt.Println(item2 == nil)
}
```
