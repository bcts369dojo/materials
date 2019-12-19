# Go Basics 演習 80 goroutine

次のコードを実行結果はどうなりますか？

ヒント: wg.Done() が実行されるタイミングに注目しましょう。この例では、タイミングはタイマーによって調整されています。 

https://play.golang.org/p/YTmUa3at-vs で動作確認できます。

```go
// bcts369道場 Go Basics 演習80 goroutine
package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {

	wg.Add(2)

	go foo()
	go bar()

	wg.Wait() // 全てのgorutineがwg.Done()をコールするまで待たされる
	fmt.Println("Fisnish!")
}

func foo() {
	for i := 0; i < 10; i++ {
		fmt.Println("Foo:", i)
		time.Sleep(3 * time.Millisecond)
	}
	wg.Done()
}

func bar() {
	for i := 0; i < 10; i++ {
		fmt.Println("Bar:", i)
		time.Sleep(20 * time.Millisecond)
	}
	wg.Done()
}
```
