# Go Basics 演習 50 map

次のコードを実行すると、どのように表示されますか？

ヒント: マップは参照型で、定義されるとゼロ値はnilになります。 nilマップへの書き込みはパニックになり、読み取りは常にゼロ値を返します。

https://play.golang.org/p/tsU7hqr-PKQ で動作確認できます。

```go
// bcts369道場 Go Basics 演習50 map
package main

import "fmt"

func main() {
	var myMap map[string]string
	fmt.Println(myMap)
	fmt.Println(myMap == nil)

    // 次のコードのコメントを外してみてください。
	// myMap["name"] = "Taro" // error
	// myMap["age"] = "30"    // error
}
```
