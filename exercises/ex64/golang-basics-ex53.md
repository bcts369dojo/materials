# Go Basics 演習 53 map

次のコードを実行すると、どのように表示されますか？

ヒント: マップの初期化と要素の追加を同時に行う方法に注目してください。

https://play.golang.org/p/77smHG9UkQb で動作確認できます。

```go
// bcts369道場 Go Basics 演習53 map
package main

import "fmt"

func main() {

	myMap := map[string]string{
		"name": "Taro",
		"age":  "30", // このカンマは必要
	}

	fmt.Println(myMap)
}
```
