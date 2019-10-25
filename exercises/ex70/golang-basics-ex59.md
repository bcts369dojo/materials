# Go Basics 演習 59 map

次のコードを実行すると、どのように表示されますか？

存在しないキーを削除しようとしてもエラーは発生しません。ですから、要素を削除する前に存在するかどうかを確認すべきです。

ヒント: mapの要素の存在判定と削除。

https://play.golang.org/p/-rf1iGJouRX で動作確認できます。

```go
// bcts369道場 Go Basics 演習59 map
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

	if value, exists := myMap["hoge"]; exists {
		fmt.Println("値が存在します。")
		fmt.Println("value: ", value)
		fmt.Println("exists: ", exists)
	} else {
		fmt.Println("値が存在しません。")
		fmt.Println("value: ", value)
		fmt.Println("exists: ", exists)
	}

	delete(myMap, "hoge") // hogeというキーは存在しない。エラーは発生する？

}
```
