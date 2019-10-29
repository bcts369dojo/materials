# Go Basics 演習 61 map

次のコードを実行すると、どのように表示されますか？

ヒント: range を使用すると、map 内の全エントリにアクセスして処理を行うことができます。

https://play.golang.org/p/ACN0n9-n94p で動作確認できます。

```go
// bcts369道場 Go Basics 演習61 map
package main

import "fmt"

func main() {

	myMap := map[string]string{
		"name": "Taro",
		"bloodtype": "A",
		"age":  "30", // このカンマは必要
	}

	for key, val := range myMap {
		fmt.Println(key, " - ", val)
	}
}
```
