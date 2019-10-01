# 学習内容

リンクが有効でない項目は検討中または準備中です。

学習の順番は基本、並び順で行ってください。

エクササイズ番号は単に通し番号です。優先順位などの意味はありません。


## Chapter 開発を行うまでの準備

まずはここから始めます。

1. [Markdown](/exercises/ex1/README.md)
2. [よく使用するUNIXコマンド](/exercises/ex12/README.md)
3. [GitHub Flow](/exercises/ex2/README.md)
4. [GitHub Issues](/exercises/ex3/README.md)
5. [GitHub Labels](/exercises/ex4/README.md)
6. [GitHub Projects](/exercises/ex5/README.md)
7. [開発環境 shell](/exercises/ex6/README.md)
8. [開発環境 git](/exercises/ex7/README.md)
9. [開発環境 golang](/exercises/ex8/README.md)


## Chapter Golang Basic

Go言語の基本を理解しましょう。

1. [Go言語チュートリアル](/exercises/ex9/README.md)
2. [演習1](/exercises/ex10/README.md)
2. [演習2](/exercises/ex11/README.md)

## Chapter Go言語 ステップ2

1. ライブラリを使用してみる
2. 自分でライブラリを作成してみる（独自パッケージ作成）
3. Go Modules
4. Makefile
5. シリアライズ
6. [WIP:環境変数をGoで使う](/exercises/ex13/README.md)


## Chapter JSON

実際のアプリ開発では、JSONというデータのフォーマットが使われています。Go言語においてJSONフォーマットのデータをどのように扱うかを学びます。
なおJSONとは、JavaScript Object Notationの略称であり、標準的なテキストベースの構造データ表現フォーマットで、JavaScript 構造データオブジェクトの表記法をベースとしています。

[JSON データの操作](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Objects/JSON)という非常に参考になる情報があるので、一読することを勧めます。

- Ex-1 JSONフォーマットのテキストデータを読み込み、表示します。
- Ex-2 JSONフォーマットのデータをGoの構造体にマッピングします。

## Chapter API

実際のアプリ開発では、さまざまな機能を自分で作るのではなく、API（Application Programming Interface）を利用することが非常に多いです。
もちろん独自でAPIを作る場合もありますが、ここではAPIを利用する方法について学びます。
APIのデータ形式はJSONを始め、GraphQLという新しいフォーマットが利用されていますが、これらにも触れていきます。

`JSON` のチャプターを終了している必要があります。

- Ex-1 為替情報（JPY, USDなど）を取得し、表示します。
- Ex-2 暗号資産の情報（BTC, ETH など）を取得し、表示します。
- Ex-3 上記を元に、1BTCあたりの日本円でいくらかを計算し、表示します。

## Chapter CLIアプリケーション

簡単なCLIアプリを数種類作成します。

### Section1

BMIを算出するCLIアプリを作成します。

- Ex-1 身長と体重から標準体重、BMIを算出します。
- Ex-2 上記に加え、算出されたBMIから肥満度を判定します。
- Ex-3 構造体とメソッドを使って書き直す
- Ex-4 テストコードを書く

### Section2

Todo（タスク）を管理するCLIアプリケーションを作成します。

- EX-1 Todoアプリの仕様。
- Ex-2 最も簡単なTodoアプリを作る。
- Ex-3 構造体とメソッドを使って書き直す。
- Ex-4 コマンドライン引数に対応する。
- Ex-5 TODO内容をJSONで管理する。
- Ex-6 テストコードを書く。

### Section3

ポモドーロCLIアプリを作成します。Chapter3のEx-７まで理解できていることが前提です。

- Ex-1 ポモドーロアプリの仕様。
- Ex-2 25分間隔でメッセージを表示するようにする。
- Ex-3 上記に加え5分後にメッセージを表示するようにする。
- Ex-4 25分後、その5分後にメッセージを表示するようにする。
- Ex-5 メッセージではなく、サウンドを鳴らすようにする。
- Ex-6 テストコードを書く。
- Ex-7 設定ファイルの内容でアプリの動作を変更する。

## Chapter Webアプリケーション

### Section1 Todoアプリ

CLIアプリで学んだTODOアプリの基本を元にWEBアプリ化して、ブラウザ経由で同様以上の機能を実装する方法を学びます。

- Ex-1 ログイン（認証）実装
- Ex-2 データ管理をDB（NoSQL）で行う
- Ex-3 キーワードなどのメタデータを追加できるようにする
- Ex-4 画像を登録できるようにする
- Ex-5 複数ユーザ対応
- Ex-6 通知
- Ex-7 クラウドサービスを利用してアプリを外部公開できるようにする
- Ex-8 マイクロサービス対応（RPC）
     - gRPC-Web

## Chapter データの永続化（データベースなど）

- Ex-1 Database Local Database
    - SQLite
    - LevelDB
- Ex-2 Database SQL
    - SQLite
    - MySQL
- Ex-3 Database NOSQL
    - LevelDB
    - Mongodb
- Ex-4 GraphQL
    - 未定

## Chapter Scraping

スクレイピング関連。


## Chapter 暗号資産

- トレードをする前に知っておくこと。
- 暗号資産の自動取引ボット
- 暗号資産取引所のアカウント作成
- 現在のレートを取得してみる
    - [GMOコインで最新レートを取得してみる](https://api.coin.z.com/docs/?javascript#ticker)
        - https://api.coin.z.com/public/v1/ticker

## Chapter Twitterボット

Twitter APIを利用したbotアプリ作成。

## Chapter Docker

主に、開発環境について。

- Ubuntu:latestを導入して、ベース環境を導入する。
- 道場が提供するインストラーを使用して、開発に必要な環境を自動インストールする。


## Chapter Cloud Development
- クラウド開発環境
    - Google Cloud
    - AWS
    - Azure
    - IBM Cloud

## Chapter マイクロサービス／サーバレス

マイクロサービス／サーバレスの基礎を学びます。


## Chapter CI
- CI（継続的インテグレーション）

主に、CircleCiを使用して、**継続的インテグレーション** について学びます。

## Chapter 認証
- OAuthまたはJWTによるユーザ認証

## Chapter 多言語対応

アプリやサービスの多言語対応について学びます。

## Chapter IoT

Internet of Thingsについて学びます。ただし、センサーなどの機材（１万円未満）を購入する必要があるので、自由選択とします。

- Raspbery Pi + センサー類


## Chapter AI

フレームワークやライブラリを使用して、簡単なAIアプリの作り方を学びます。本格的な解析方法には触れません。

- 遺伝的アルゴリズム
- 機械学習
- 深層学習


## Chapter Debug

VSCodeを使用したデバッグの方法を学びます。

## Chapter Create My Site

自己紹介や、経歴、ポートフォリオを紹介できる自分用のサイトを無料で作る方法。

- Ex-1 Github Pagesを使用して簡単にマイサイトを作る
- Ex-2 Github PagesとHugoを使用して簡単にマイサイトを作る

## Chapter ポートフォリオ動作環境

作成した自分のアプリを公開するにはサーバーなどの動作環境が必要です。ここでは、無料、有料で使えるサービスを利用して、アプリを登録、公開する方法を学びます。

- Heroku
- Amazon Lightsale
- Lolipop

## モバイルアプリ対応

PWA、HTML5、Hybrid、Native

- Ex-1 モバイルアプリの種類と開発方法について

## 検討中

- セキュリティ
- どんなサービスを作りたいのか？ それについてディスカッションする方法。
- 仮想案件に対して、提案書、見積書、概要設計書を提出する。
- 開発中の失敗を体験し、どのように対応するのか体験するには？
- 自分の得意分野をつくるには？
