# Go Basics 演習 68 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 構造体はネストできます。

https://play.golang.org/p/vpRnVWuomJ8 で動作確認できます。

```go
// bcts369道場 Go Basics 演習68 struct
package main

import (
	"fmt"
)

type person struct {
	Name string
	Age  int
}

type member struct {
	person
	MemberID string
}

func main() {
	p1 := member{
		person: person{
			Name: "Taro",
			Age:  20,
		},
		MemberID: "001",
	}

	p2 := member{
		person: person{
			Name: "Ichiro",
			Age:  19,
		},
		MemberID: "002",
	}

	fmt.Println(p1.Name, p1.Age, p1.MemberID)
	fmt.Println(p2.Name, p2.Age, p2.MemberID)
}
```
