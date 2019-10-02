
# Go Basics 演習2

Go言語の基礎の演習では、Githubのプルリクエストは使用しません、SlackのDMにて回答をご連絡ください。

次のコードを実行すると、どのように表示されますか？

ヒント： 以下のコードは自動的に変数に割り当てられた「型」が表示されます。

https://play.golang.org/p/qHVtMewKMca で動作確認できます。

実行せずに、頭で考えて答えてください。

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

	fmt.Printf("%T \n", a)
	fmt.Printf("%T \n", b)
	fmt.Printf("%T \n", c)
	fmt.Printf("%T \n", d)
	fmt.Printf("%T \n", e)
	fmt.Printf("%T \n", f)
	fmt.Printf("%T \n", g)
}

```