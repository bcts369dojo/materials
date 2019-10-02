# Go Basics 演習4 ゼロ値

次のコードを実行すると、どのように表示されますか？

ヒント： 以下のコードは自動的に変数に割り当てられた「値」が表示されます。

https://play.golang.org/p/S_ifUxgRR5F で動作確認できます。

実行せずに、頭で考えて答えてください。

```go
package main

import "fmt"

func main() {

    // 初期化宣言されていない変数
	var a int
	var b string
	var c float64
	var d bool

	fmt.Printf("%v \n", a)
	fmt.Printf("%v \n", b)
	fmt.Printf("%v \n", c)
	fmt.Printf("%v \n", d)

	fmt.Println()
}
```

## 参考情報

[ゼロ値を使おう #golang](https://qiita.com/tenntenn/items/c55095585af64ca28ab5)