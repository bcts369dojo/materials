# Go Basics 演習 63 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 「値型」としてメソッド定義されたものが「値レシーバ」です。 関数定義は func (レシーバ値 レシーバ型) 関数名という形になります。

https://play.golang.org/p/ZtCBHng4OiB で動作確認できます。

```go
// bcts369道場 Go Basics 演習63 struct

package main

import "fmt"

type person struct {
        first string
        last  string
        age   int
}

// 値レシーバ
// person という型のstructに対して fullName() というメソッドを定義。
func (p person) fullName() string {
        return p.first + p.last
}

func main() {
        p1 := person{"Ichro", "Tanaka", 20}
        p2 := person{"Taro", "Yamada", 18}
        fmt.Println(p1.first, p1.last, p1.age)
        fmt.Println(p2.first, p2.last, p2.age)
        fmt.Println(p1.fullName())
        fmt.Println(p2.fullName())
}
```
