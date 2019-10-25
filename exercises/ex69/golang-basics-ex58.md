# Go Basics 演習 58 map

次のコードを実行すると、どのように表示されますか？

ヒント: mapの要素の存在判定

https://play.golang.org/p/yHsMibS1FnT で動作確認できます。

```go
// bcts369道場 Go Basics 演習58 map
package main

import "fmt"

func main() {

	myMap := map[string]string{
		"name": "Taro",
		"age":  "30", // このカンマは必要
	}

	myMap["bloodtype"] = "AB" // 初期化後は要素を追加できます
	fmt.Println(myMap)

	myMap["bloodtype"] = "A" // 内容も変更できます
	fmt.Println(myMap)

	// --- この2行をコメントした場合の動作も確認してください。
	delete(myMap, "bloodtype") // 要素を削除
	fmt.Println(myMap)


	if value, exists := myMap["bloodtype"]; exists {
		fmt.Println("値が存在します。")
		fmt.Println("value: ", value)
		fmt.Println("exists: ", exists)
	} else {
		fmt.Println("値が存在しません。")
		fmt.Println("value: ", value)
		fmt.Println("exists: ", exists)
	}
}
```
