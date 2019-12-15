# Go Basics 演習 66 struct

次のコードを実行すると、どのように表示されますか？

ヒント: 次の公式ドキュメントを読むか `json.Marshal` でググってみましょう。

- https://golang.org/src/encoding/json/encode.go?s=6471:6514#L148
- https://xn--go-hh0g6u.com/pkg/encoding/json/#Marshal

https://play.golang.org/p/_CR6QgFgIaT で動作確認できます。

```go
// bcts369道場 Go Basics 演習66 struct
package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	Name string
	Age  int
}

func main() {
	taro := person{"Taro", 20}
	bs, _ := json.Marshal(taro)
	fmt.Println(bs)
	fmt.Printf("%T \n", bs)
	fmt.Println(string(bs))
}
```
