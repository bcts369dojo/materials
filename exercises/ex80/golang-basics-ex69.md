# Go Basics 演習 69 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 構造体の初期化方法は複数あります。

https://play.golang.org/p/etqCno8Dt5e で動作確認できます。

```go
// bcts369道場 Go Basics 演習69 struct
package main

import "fmt"

type person struct {
	name string
	age  int
}

func main() {
	p1 := &person{"Taro", 20}
	fmt.Println(p1)
	fmt.Printf("%T\n", p1)
	fmt.Println(p1.name)
	fmt.Println(p1.age)

	fmt.Println("-------")

	p2 := new(person)
	p2.name = "Ichro"
	p2.age = 21
	fmt.Println(p1)
	fmt.Printf("%T\n", p2)
	fmt.Println(p2.name)
	fmt.Println(p2.age)
}

```
