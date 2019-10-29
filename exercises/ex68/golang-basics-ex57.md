# Go Basics 演習 57 map

次のコードを実行すると、どのように表示されますか？

ヒント: mapの要素削除。

https://play.golang.org/p/LMp0lmleCkN で動作確認できます。

```go
// bcts369道場 Go Basics 演習57 map
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

	delete(myMap, "bloodtype") // 要素を削除
	fmt.Println(myMap)
}
```
