# Go Basics 演習3

次のコードをmain関数で実行すると、どのように表示されますか？

`package main` と `import ("fmt")` が記述されていることを前提とします。

https://play.golang.org/p/XeOXtmP1-We で動作確認できます。

実行せずに、頭で考えてください。

```go
fmt.Printf("%t\n", true)
fmt.Printf("%d\n", 123)
fmt.Printf("%b\n", 14)
fmt.Printf("%x\n", 456)
fmt.Printf("%f\n", 78.9)
fmt.Printf("%e\n", 123400000.0)
fmt.Printf("%E\n", 123400000.0)
fmt.Printf("%s\n", "\"string\"")
fmt.Printf("%q\n", "\"string\"")
fmt.Printf("|%6d|%6d|\n", 12, 345)
fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)
fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45)
fmt.Printf("|%6s|%6s|\n", "foo", "b")
fmt.Printf("|%-6s|%-6s|\n", "foo", "b")
s := fmt.Sprintf("a %s", "string")
fmt.Println(s)
```