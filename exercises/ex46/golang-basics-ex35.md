# Go Basics 演習 35 Function

次のコードを実行すると、どのように表示されますか？

ヒント：visit 関数の第２引数が関数である点に注目してください。

https://play.golang.org/p/U01Gj5xe3sd で動作確認できます。

```go
package main

import "fmt"

func visit(numbers []int, callback func(int)) {
	for _, n := range numbers {
		callback(n)
	}
}

func main() {
	visit([]int{1, 2, 3, 4}, func(n int) {
		fmt.Println(n)
	})
}
```
