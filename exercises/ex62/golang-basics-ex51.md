# Go Basics 演習 51 map

次のコードを実行すると、どのように表示されますか？

ヒント: マップの初期化の１つの方法として、 `make関数` を使うことができます。

https://play.golang.org/p/_5fRAiqR1MR で動作確認できます。

```go
// bcts369道場 Go Basics 演習51 map
package main

import "fmt"

func main() {

	var myMap = make(map[string]string)
	myMap["name"] = "Taro"
	myMap["age"] = "30"
	fmt.Println(myMap)
}
```
