# 学習内容

リンクが有効でない項目は検討中であり、順番も未定。

学習単位（パート、チャプター、セクション、エクササイズ、レッスン）については未だに悩んでいるので、今後も構成が変わる可能性があります。また、パートやチャプターなどの大分類については、ナンバリングすると追加や、変更などの管理が難しくなるので、ネーミングで管理するかもしれません。

チャプター単位で書いていきますが、パートまで必要と感じた場合は、構成を変更します。
なお、一般的には `Lesson` と使われるかもしれませんが、本道場では `Exercise` と表現します。

## Chapter1

基礎の基礎、まずはここから始めます。

- [Exercise1 Markdown](./exercises/exercise1)
- [Exercise2 GitHub Flow](./exercises/exercise2)
- [Exercise3 GitHub Issues](./exercises/exercise3)
- [Exercise4 GitHub Labels](./exercises/exercise4)
- [Exercise5 GitHub Projects Part1](./exercises/exercise5)
- [Exercise6 Develop Environment shell](./exercises/exercise6)
- [Exercise7 Develop Environment git](./exercises/exercise7)
- [Exercise8 Develop Environment golang](./exercises/exercise8)
- [Exercise12 よく使用するUNIXコマンド](./exercises/exercise12)


## Chapter Create My Site

自己紹介や、経歴、ポートフォリオを紹介できる自分用のサイトを無料で作る方法。

- Ex-1 Github Pagesを使用して簡単にマイサイトを作る
- Ex-2 Github PagesとHugoを使用して簡単にマイサイトを作る

## Chapter Golang Tutorial

Go言語の基本を理解しましょう。

- [Ex-1 Go Basics1](./exercises/exercise9)
- [Ex-2 Go Basics2](./exercises/exercise10)
- [Ex-3 Go Basics3](./exercises/exercise11)
- Ex-4 理解度チェック１
- Ex-5 Go Basics Methods and interfaces
- Ex-6 理解度チェック２
- Ex-7 Go Basics Concurrency
- Ex-8 理解度チェック３
- ライブラリを使用してみる
- 自分でライブラリを作成してみる（独自パッケージ作成）
- Go Modules
- Makefile
- [WIP:Exercise13 環境変数をGoで使う](./exercises/exercise13)

## JSON

実際のアプリ開発では、JSONというデータのフォーマットが使われています。Go言語においてJSONフォーマットのデータをどのように扱うかを学びます。

## API

実際のアプリ開発では、さまざまな機能を自分で作るのではなく、API（Application Programming Interface）を利用することが非常に多いです。
もちろん独自でAPIを作る場合もありますが、ここではAPIを利用する方法について学びます。
APIのデータ形式はJSONを始め、GraphQLという新しいフォーマットが利用されていますが、これらにも触れていきます。

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
   - Ver2.1 ログイン（認証）実装
   - Ver2.2 データ管理をDB（NoSQL）で行う
   - Ver2.3 キーワードなどのメタデータを追加できるようにする
   - Ver2.4 画像を登録できるようにする
   - Ver2.5 複数ユーザ対応
   - Ver2.6 通知
   - Herokuなどでアプリを外部公開できるようにする
   - Ver3.0 クラウド対応（Google Cloud）
   - Ver4.0 マイクロサービス対応（RPC）
        - gRPC-Web
   - Ver5.0 ブロックチェーン対応（ETH）

## Chapter データの永続化（データベースなど）

- Database Local Database
- Database SQL
- Database NOSQL
- GraphQotL

## Chapter Blockchain

ブロックチェーンを利用したDAppsの開発関連。

### Section1 Ethereum

### Section2 Nem

## Chapter Scraping

スクレイピング関連。


## Chapter 暗号資産

- トレードをする前に知っておくこと。
- 暗号資産の自動取引ボット
- 暗号資産取引所のアカウント作成

## Chapter Twitterボット

Twitter APIを利用したbotアプリ作成。

## Chapter Docker

主に、開発環境について。

- Ubuntu:latestを導入して、ベース環境を導入する。
- 道場が提供するインストラーを使用して、開発に必要な環境を自動インストールする。


## Cloud Development
- クラウド開発環境
    - Google Cloud
    - AWS

## Chapter CI
- CI（継続的インテグレーション）

主に、CircleCiを使用して、**継続的インテグレーション** について学びます。

## Chapter 認証
- OAuthまたはJWTによるユーザ認証

## Chapter IoT

Internet of Thingsについて学びます。ただし、センサーなどの機材（１万円未満）を購入する必要があるので、自由選択とします。

- Raspbery Pi


## Chapter AI

フレームワークやライブラリを使用して、簡単なAIアプリの作り方を学びます。


## Chapter Debug

VSCodeを使用したデバッグの方法を学びます。

## Chapter ポートフォリオ動作環境

作成した自分のアプリを公開するにはサーバーなどの動作環境が必要です。ここでは、無料、有料で使えるサービスを利用して、アプリを登録、公開する方法を学びます。

- Heroku
- Amazon Lightsale
- Lolipop


## 検討中

- 仮想案件に対して、提案書、見積書、概要設計書を提出する。
- 開発中の失敗を体験し、どのように対応するのか体験するには？

