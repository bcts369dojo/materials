# Go Basics 演習 79 goroutine

次のコードを実行結果はどうなりますか？

ヒント: WaitGroupについてはググってみましょう。またfoo() bar() の実行順序に注目しましょう 

https://play.golang.org/p/H8n3lXODCSJ で動作確認できます。

```go
// bcts369道場 Go Basics 演習79 goroutine
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {

	wg.Add(2)
	fmt.Println("Before")
	go foo()
	go bar()
	fmt.Println("After")
	wg.Wait() // 全てのgorutineがwg.Done()をコールするまで待たされる
	fmt.Println("Finish!")
}

func foo() {
	for i := 0; i < 5; i++ {
		fmt.Println("Foo:", i)
	}
	wg.Done()
	fmt.Println("done1..")
}

func bar() {
	for i := 0; i < 5; i++ {
		fmt.Println("Bar:", i)
	}
	wg.Done()
	fmt.Println("done2..")
}
```
