# Go Basics 演習 56 map

次のコードを実行すると、どのように表示されますか？

ヒント: mapの値変更。

https://play.golang.org/p/foRsYv5Arq9 で動作確認できます。

```go
// bcts369道場 Go Basics 演習56 map
package main

import "fmt"

func main() {

	myMap := map[string]string{
		"name": "Taro",
		"age":  "30", // このカンマは必要
	}

	myMap["bloodtype"] = "AB" // 初期化後は要素を追加できます
	fmt.Println(myMap)

	myMap["bloodtype"] = "A"  // 内容も変更できます
	fmt.Println(myMap)
}

```
