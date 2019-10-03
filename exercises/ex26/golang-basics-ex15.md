# Go Basics 演習15  定数

次のコードを実行すると、 どのように表示されますか？

https://play.golang.org/p/oNW24L6v4Gb で動作確認できます。

ヒント： 識別子 `iota` 、`fmt.Stringerインターフェース` について理解しておきましょう

```go
// bcts369道場 Go Basics 演習15 定数
package main

import "fmt"

type Color int

const (
	Red Color = iota + 1
	Green
	Blue
)

// fmt.Stringer インターフェースを実装
func (c Color) String() string {
	switch c {
	case Red:
		return "赤"
	case Green:
		return "緑"
	case Blue:
		return "青"
	default:
		return "Unknown"
	}
}
```

