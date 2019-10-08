# Go Basics 演習 32 Function

次のコードを実行すると、どのように表示されますか？

ヒント： average 関数は引数として可変引数として宣言しており、引数の数をしていません。使いどころは限定されますが便利な機能です。どんな場面で可変引数を使えばよいか考えてみてください。

https://play.golang.org/p/zB3f_KChA7V で動作確認できます。

```go
// bcts369道場 Go Basics 演習32 Function
package main

import "fmt"

func main() {
	n := average(10.0, 20.0, 30.0, 40.0, 50.0, 60)
	fmt.Println(n)
}

func average(sf ...float64) float64 {
	fmt.Println(sf)
	fmt.Printf("%T \n", sf)
	var total float64
	for _, v := range sf {
		total += v
	}
	return total / float64(len(sf))
}
```
