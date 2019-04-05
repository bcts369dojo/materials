# Exercise6 開発環境構築（shell)

## はじめに

本道場ではターミナルを非常に多く使います。そのため、ターミナルの使い勝手に大きく影響を与える`シェル`の選択は非常に重要です。
普通に使う分には、初期導入されている`Bash`でも問題ありませんが、`Zsh`を使用すると、大きく機能拡張され、便利な機能がたくさん使えるようになります。また本道場でターミナルの操作説明をする場合は、`Zsh`が導入されていることを前提として行います。

エディタ同様、強制はしませんので、導入するかどうかはご自分の判断でお願いします。

`Zsh`を導入したら、設定プラットフォームの`Oh My ZSH!`を導入します。`導入フレームワーク`という言葉は聞き慣れていないかもしれませんが、要するに自分で複雑な設定をしなくても、フレームワークが便利でよく使われる機能を最初から提供してくれるというすぐれものです。

同類のフレームワークがいくつかありますが、道場では`Oh My ZSH!`を使用します。

これらの導入方法はググればたくさんありますので、参考情報を始め、幾つか見て回ると良いと思います。
ちなみに、テーマを変更したり、フォントをインストールする必要はありませんが、やりたい人はどうぞ。

なお、`~/.zshrc`の`plugins`設定は、次のように変更することをおすすめします。


macOSの場合

```
plugins=(
  git gitignore github go golang python virtualenv node yarn npx rsync docker docker-compose docker-machine zsh_reload
)
```

Ubuntuの場合

```
plugins=(
  git gitignore github go golang python virtualenv ubuntu node yarn npx rsync docker docker-compose docker-machine zsh_reload
)
```

## 理解度チェック

正しくインストールされているか確認します。プルリクエストは必要ないので、Slackに連絡ください。


### シェルがBashからZshに変更されているかどうか？

次のコマンドをターミナルで実行し、結果を教えてください。

```shell
echo $SHELL
```

### 設定フレームワークである`Oh My ZSH!`が正しくインストールされているか？

次のコマンドをターミナルで実行し、結果を教えてください。

```shell
ls ~/.oh-my-zsh
```

## 参考情報へのリンク

- [How to Configure your macOs Terminal with Zsh like a Pro](https://medium.freecodecamp.org/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156)
- [Oh My Zsh - a delightful & open source framework for Z-Shell](https://ohmyz.sh/)
- https://qiita.com/Angelan1720/items/60431c85592fe90fcdd5
- https://qiita.com/rspepe/items/9e30e698c4fc3e90891d
- https://github.com/sorin-ionescu/prezto

```sh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
