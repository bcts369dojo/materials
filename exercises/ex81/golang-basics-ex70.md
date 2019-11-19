# Go Basics 演習 70 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 構造体のメンバーの先頭が大文字で始まる場合とそうでない場合の挙動が異なります。 notExported を NotExported に変更して確認してみてください。

https://play.golang.org/p/-9ZfFF-GwHG で動作確認できます。

```go
// bcts369道場 Go Basics 演習70 struct
package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	Name        string
	Age         int
	notExported int
}

func main() {
	p1 := person{"Taro", 20, 001}
	bs, _ := json.Marshal(p1)
	fmt.Println(bs)
	fmt.Printf("%T \n", bs)
	fmt.Println(string(bs))
}
```
