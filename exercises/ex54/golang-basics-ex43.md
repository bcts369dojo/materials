# Go Basics 演習 43 slice

次のコードを実行すると、どのように表示されますか？

ヒント: スライスの Capacity に注目してください。

https://play.golang.org/p/Jc1Dgmq5e3D 動作確認できます。

```go
package main

import "fmt"

func main() {

	mySlice := make([]int, 0, 3)

	fmt.Println("-----------------")
	fmt.Println(mySlice)
	fmt.Println(len(mySlice))
	fmt.Println(cap(mySlice))
	fmt.Println("-----------------")

	for i := 0; i < 10; i++ {
		mySlice = append(mySlice, i)
		fmt.Println("Len:", len(mySlice), "Capacity:", cap(mySlice), "Value: ", mySlice[i])
	}
}
```
