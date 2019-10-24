# Go Basics 演習 55 map

次のコードを実行すると、どのように表示されますか？

ヒント: mapのサイズ。

https://play.golang.org/p/81R_kvZusLL で動作確認できます。

```go
// bcts369道場 Go Basics 演習55 map
package main

import "fmt"

func main() {

	myMap := map[string]string{
		"name": "Taro",
		"age":  "30", // このカンマは必要
	}

	myMap["bloodtype"] = "AB" // 初期化後は要素を追加できます

	fmt.Println(len(myMap))
}

```
