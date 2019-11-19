# Go Basics 演習 72 struct

次のコードを実行すると、どのように表示されますか？

ヒント: go の構造体にはタグによって実行時に参照可能なメタ情報を付与することができます。 json.Unmarshal 関数は、JSON をでコードし、構造体のメンバーにマッピングします。この json.Unmarshal 関数は非常によく使いますので使い方をマスターしておきましょう。

https://play.golang.org/p/jRvuNh9TM5K で動作確認できます。

```go
// bcts369道場 Go Basics 演習72 struct
package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	First string
	Last  string
	Age   int `json:"my_age"`
}

func main() {
	var p1 person
	fmt.Println(p1.First)
	fmt.Println(p1.Last)
	fmt.Println(p1.Age)

	bs := []byte(`{"First":"Taro", "Last":"Yamada", "my_age":20}`) // JSON
	json.Unmarshal(bs, &p1) // jsonタグによりデコードされ、p1に格納されます

	fmt.Println("--------------")
	fmt.Println(p1.First)
	fmt.Println(p1.Last)
	fmt.Println(p1.Age)
	fmt.Printf("%T \n", p1)
}
```
