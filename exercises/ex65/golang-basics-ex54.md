# Go Basics 演習 54 map

次のコードを実行すると、どのように表示されますか？

ヒント: マップの初期化と要素の追加を同時に行う方法に注目してください。また初期化後は要素を追加できます。

https://play.golang.org/p/yc2Z9BzAYMF で動作確認できます。

```go
// bcts369道場 Go Basics 演習54 map
package main

import "fmt"

func main() {

	myMap := map[string]string{
		"name": "Taro",
		"age":  "30", // このカンマは必要
	}

	myMap["bloodtype"] = "AB" // 初期化後は要素を追加できます

	fmt.Println(myMap)
}

```
