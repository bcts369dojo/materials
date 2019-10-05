# Go Basics 演習24 Switch文

次のコードを実行すると、どのように表示されますか？

このように if - else と同じ様に使うこともできます。

https://play.golang.org/p/lnJvVFyJExD で動作確認できます。


```go
package main

import "fmt"

func main() {

	myFriendsName := "Sakura2"

	switch {
	case len(myFriendsName) == 2:
		fmt.Println("名前の長さが2です")
	case myFriendsName == "Jiro":
		fmt.Println("Jiro")
	case myFriendsName == "Taro":
		fmt.Println("Taro")
	case myFriendsName == "Yoko", myFriendsName == "Sakura":
		fmt.Println("あなたの名前はYoko またはSkuraです")
	default:
		fmt.Println("マッチしませんでした")
	}
}
```
