# Go Basics 演習 37 Function

次のコードを実行すると、どのように表示されますか？

ヒント：defer は関数を抜ける直前に実行されます。

https://play.golang.org/p/4rsczXk4Xz1 で動作確認できます。

```go
package main

import "fmt"

func func1() {
	fmt.Println("func1")
}

func func2() {
	fmt.Println("func2")
}

func main() {
	fmt.Println("1")
	defer func1()
	fmt.Println("2")
	func2()
	fmt.Println("3")
}
```
