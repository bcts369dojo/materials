# Go Basics 演習 33 Function

次のコードを実行すると、どのように表示されますか？

ヒント：n := average(data...) の行に注目してください。 演習 31 と何が違いますか？

https://play.golang.org/p/ewsruiZcRR_Z で動作確認できます。

```go
// bcts369道場 Go Basics 演習33 Function
package main

import "fmt"

func main() {
	data := []float64{10, 20, 30, 40, 50, 60}
	n := average(data...)
	fmt.Println(n)
}

func average(sf ...float64) float64 {
	total := 0.0
	for _, v := range sf {
		total += v
	}
	return total / float64(len(sf))
}
```
