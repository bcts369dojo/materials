# Go Basics 演習 76 interface

次のコードを実行すると、どのように表示されますか？

ヒント: interface{}型は全ての型を格納可能です。

https://play.golang.org/p/IHNuRbocSCh で動作確認できます。

```go
// bcts369道場 Go Basics 演習76 interface
package main

import "fmt"

type animal struct {
	sound string
}

type dog struct {
	animal
	name string
}

type cat struct {
	animal
	age int32
}

func specs(i interface{}) {
	fmt.Println(i)
}

func main() {
	d := dog{animal{"わんわん"}, "Pochi"}
	c := cat{animal{"にゃお"}, 3}
	specs(d)
	specs(c)
}
```
