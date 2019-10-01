# Go言語基礎の理解度チェック

次のコードを実行すると、どのように表示されますか？

実行せずに考えて答えてください。回答はSlackのDMでお願いします。

<!-- https://github.com/GoesToEleven/GolangTraining/blob/master/03_variables/01_shorthand/01/main.go -->

```go
package main

import "fmt"

func main() {

	a := 10　
	b := "golang"
	c := 9.99
	d := true
	e := "Hello"
	f := `Do you like golang?`
	g := 'A'

	fmt.Printf("%v \n", a)
	fmt.Printf("%v \n", b)
	fmt.Printf("%v \n", c)
	fmt.Printf("%v \n", d)
	fmt.Printf("%v \n", e)
	fmt.Printf("%v \n", f)
	fmt.Printf("%v \n", g)
}

```

どのような型が表示されますか？


<!-- https://github.com/GoesToEleven/GolangTraining/blob/master/03_variables/01_shorthand/02/main.go -->

```go
package main

import "fmt"

func main() {

	a := 10
	b := "golang"
	c := 9.99
	d := true
	e := "Hello"
	f := `Do you like golang?`
	g := 'A'

	fmt.Printf("%T \n", a)
	fmt.Printf("%T \n", b)
	fmt.Printf("%T \n", c)
	fmt.Printf("%T \n", d)
	fmt.Printf("%T \n", e)
	fmt.Printf("%T \n", f)
	fmt.Printf("%T \n", g)
}

```