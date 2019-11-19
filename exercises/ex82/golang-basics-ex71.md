# Go Basics 演習 71 struct

次のコードを実行すると、どのように表示されますか？

ヒント: go の構造体にはタグによって実行時に参照可能なメタ情報を付与することができます。 json.Marshal 関数は、「json:」とタグ付けされたメタ情報を読み込みますが、タグが存在しない場合は変数名が使用されます。

https://play.golang.org/p/gBJZSWHbJtD で動作確認できます。

```go
// bcts369道場 Go Basics 演習71 struct
package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	First string                 // jsonタグが存在しないので、メンバ名が使用される
	Last  string `json:"-"`      // 無視される
	Age   int    `json:"my_age"` // jsonタグが存在するので、my_ageが使用される
}

func main() {
	p1 := person{"Taro", "Yamada", 20}
	bs, _ := json.Marshal(p1)
	fmt.Println(string(bs))
}
```
