# Exercise7 開発環境構築（git)

## はじめに

gitは現在最も使われているバージョン管理システムです。まずはこのgitのことを知る必要がありますが、一度に全てを理解するのは不可能です。まずは一般的な通常業務で必要なコマンド操作ができればOKだと思います。また、GitHubが`GitHub Desktop`というGUIツールを出しており、これを使えば、煩雑な作業をしなくとも簡単にバージョン管理ができるようになります。

インストールの詳細方法は、参考情報へのリンクを確認してみてください。

### macOSの場合

- HomeBrewをインストール。
- HomeBrewを使って最新のgitをインストール。
- HomeBrewを使ってインストールしたgitを使うために、PATHの変更を`~/.zshrc`に記述する。
- GitHub Desktopをインストールする。

### Ubuntu系OSの場合

- aptパッケージマネージャを使用して最新のgitをインストールする。
- gitkrakenをインストール（GitHub Desktopほどではないが便利）。

## 理解度チェック

次のコマンドの結果を伝えてください。

### macOSの場合
- HomeBrewのバージョン
    ```shell
    brew --version
    ```
- git関連情報の表示
    ```shell
    brew info git
    ```

### Ubuntu系OSの場合
- gitのバージョン
    ```shell
    git version
    ```
- git関連情報の表示
    ```shell
    apt show git
    ```

## 参考情報へのリンク

- [Git - Book](https://git-scm.com/book/ja/v2/)
- [macOS 用パッケージマネージャー — macOS 用パッケージマネージャー](https://brew.sh/index_ja)
- [How To Install Git on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04-quickstart)
- [macOS Mojave で Git を Homebrew 管理下に変更したときの顛末 - Qiita](https://qiita.com/H-R3N/items/45f98e8242899093c7e6)

