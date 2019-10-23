# Go Basics 演習 52 map

次のコードを実行すると、どのように表示されますか？

コメントになっている `make関数` を使わない方法でも試してみてください。

ヒント: 今回もマップの初期化の方法に注目してください。

https://play.golang.org/p/ruvMXbyciCv で動作確認できます。

```go
// bcts369道場 Go Basics 演習52 map
package main

import "fmt"

func main() {

	myMap := make(map[string]string)
	// myMap := map[string]string{}

	myMap["name"] = "Taro"
	myMap["age"] = "30"
	fmt.Println(myMap)
}
```
