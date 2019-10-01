# Go Basics 演習1

Go言語の基礎の演習では、Githubのプルリクエストは使用しません、SlackのDMにて回答をご連絡ください。

次のコードを実行すると、どのように表示されますか？

実行せずに、頭で考えて答えてください。

ヒント： 以下のコードは自動的に変数に割り当てられた「値」が表示されます。


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