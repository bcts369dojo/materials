# Go Basics 演習1

次のコードを実行すると、どのように表示されますか？

ヒント： 以下のコードは自動的に変数に割り当てられた「値」が表示されます。

https://play.golang.org/p/nbizqVcuyCE で動作確認できます。

実行せずに、頭で考えてください。

```go
package main

import "fmt"

func main() {
	a := 10
	b := "golang"
	c := 9.99
	d := true
	e := "Hello"
	f := `Do you like golang?`
	g := 'A'

	fmt.Printf("%v \n", a)
	fmt.Printf("%v \n", b)
	fmt.Printf("%v \n", c)
	fmt.Printf("%v \n", d)
	fmt.Printf("%v \n", e)
	fmt.Printf("%v \n", f)
	fmt.Printf("%v \n", g)
}

```