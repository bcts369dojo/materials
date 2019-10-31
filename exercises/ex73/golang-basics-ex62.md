# Go Basics 演習 62 struct

次のコードを実行すると、どのように表示されますか？

https://play.golang.org/p/_zYQKhvicnC で動作確認できます。

```go
// bcts369道場 Go Basics 演習62 struct

package main

import "fmt"

type person struct {
        first string
        last  string
        age   int
}

func main() {
        p1 := person{"Ichro", "Tanaka", 20}
        p2 := person{"Taro", "Yamada", 18}
        fmt.Println(p1.first, p1.last, p1.age)
        fmt.Println(p2.first, p2.last, p2.age)
}
```
