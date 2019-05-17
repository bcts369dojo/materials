# GitHubでリポジトリを複製（クローン）する方法

GitHubではリポジトリを複製（クローン）する方法がいくつかありますが、GitHubが推奨している**HTTPS URLを使用したクローン作成**について説明します。道場ではこの方法を採用します。

アカウントにサインインしているときにリポジトリを表示すると、プロジェクトを自分のコンピュータに複製するために使用できるURLが、リポジトリの詳細の下に表示されます。

![clone](https://help.github.com/assets/images/help/repository/remotes-url.png)

リモートURLの設定または変更については、「リモートURLの変更 」を参照してください。

`https://`で始まるクローンURLは、パブリックおよびプライベートのすべてのリポジトリで利用できます。またファイアウォールやプロキシの内側にいる場合でも、これらのURLはどこでも機能します。

SSH URLを使用してgit clone 、 git fetch 、 git pull 、またはgit pushでリモートリポジトリにアクセスすると、パスワードの入力を求められ、 SSHキーのパスフレーズを入力する必要があります。

HTTPS URLを使用してリモートリポジトリに次のコマンドを実行すると、GitHubのユーザー名とパスワードが求められます。

- git clone
- git fetch
- git pull
- git push

2要素認証を有効にした場合は、HTTPS Gitのパスワードを入力する代わりに、個人用アクセストークン（`personal access token`）を入力する必要があります。このドキュメントでは説明しません。


GitがGitHubと通信するたびにGitHubのユーザー名とパスワードを記憶するように、認証情報ヘルパーを使用できます 。

これにより、毎回ユーザ名とパスワードを入力する必要が軽減されます。

コマンドラインでGitHubの認証を受けずにリポジトリのクローンを作成するには、代わりにGitHubデスクトップを使用してクローンを作成します。



----

## GitでGitHubのパスワードをキャッシュする

[HTTPSを使用してGitHubリポジトリを複製する](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/articles/which-remote-url-should-i-use&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhh_lt33caGLQInlOYZJTIeeSnChLg)場合は、GitHubと通信するたびにGitHubのユーザー名とパスワードを覚えておくようにGitに伝えるために`認証ヘルパー`を使用できます。

**ヒント：**認証情報ヘルパーを使用するにはGit  **1.7.10**以降が必要です。

Gitがしばらくの間パスワードをメモリに保存するように、認証情報ヘルパーをオンにします。  デフォルトでは、Gitは15分間あなたのパスワードをキャッシュします。

1.  ターミナルで、次のように入力します。

     `$ git config --global credential.helper cache # Set git to use the credential memory cache`

2.  デフォルトのパスワードキャッシュタイムアウトを変更するには、次のように入力します。

     `$ git config --global credential.helper 'cache --timeout=3600' # Set the cache to timeout after 1 hour (setting is in seconds)`



----

## 2要素認証（2FA）でアカウントを保護する

サインイン時にパスワードに加えて認証コードを要求するようにGitHubアカウントを設定できます。

### [二要素認証について](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/about-two-factor-authentication&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhiuqGKcjRYBo4IMdhKTR4hIIdUb_A)

2要素認証（2FA）は、Webサイトやアプリにログインするときに使用される追加のセキュリティ層です。  2FAでは、ユーザー名とパスワードを使用してログインし、自分だけが知っているかアクセスできる別の形式の認証を提供する必要があります。

### [二要素認証の設定](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/configuring-two-factor-authentication&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhha_eVSzs-Gt3iQm0M5RD3ZvlDX-w)

モバイルアプリまたはテキストメッセージを使用して2要素認証を構成できます。  FIDO U2Fを使用してセキュリティキーを追加することもできます。

### [2要素認証の回復方法を構成する](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/configuring-two-factor-authentication-recovery-methods&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhi5tB5_L4uiOW6NHL7LpgsAS-oB7g)

2要素認証の認証情報を紛失した場合にアカウントにアクセスするためのさまざまな回復方法を設定できます。

### [2要素認証を使用してGitHubにアクセスする](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/accessing-github-using-two-factor-authentication&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhhdDaJTtYyN2GMOUYhEAYDDHAPR_g)

2FAを有効にすると、GitHubにサインインまたは認証するときに、2FA認証コードとパスワードを入力するよう求められます。

### [2FAの認証情報を紛失した場合のアカウントの回復](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/recovering-your-account-if-you-lose-your-2fa-credentials&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhjI7TLeOl8MPfVIAK6rbbBknz3VZQ)

2要素認証の認証情報にアクセスできない場合は、自分のアカウントへのアクセスを取り戻すために、復旧コード、または設定している場合は別の復旧オプションを使用できます。

### [モバイルデバイス用の2要素認証の配信方法を変更する](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/changing-two-factor-authentication-delivery-methods-for-your-mobile-device&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhg2FpGGh3JDL0QbST62FOG1INX6NQ)

あなたは、テキストメッセージまたはモバイルアプリケーションを介して認証コードの受信を切り替えることができます。

### [SMS認証がサポートされている国](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/countries-where-sms-authentication-is-supported&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhiytzY9auX5qtg5SiE8o_SF8S4q_w)

配信成功率のために、GitHubは特定の国のためにSMSによる二要素認証のみをサポートします。

### [個人アカウントの2要素認証を無効にする](https://translate.googleusercontent.com/translate_c?depth=1&hl=ja&rurl=translate.google.com&sl=en&sp=nmt4&tl=ja&u=https://help.github.com/en/articles/disabling-two-factor-authentication-for-your-personal-account&xid=17259,15700023,15700186,15700191,15700253,15700256,15700259&usg=ALkJrhiQ_ULJzCTJgYfLiXryO-G9eiXcxw)

個人アカウントの2要素認証を無効にすると、所属する組織へのアクセスが失われる可能性があります。

## リンク

- [Caching your GitHub password in Git](https://help.github.com/en/articles/caching-your-github-password-in-git)
- [Creating a personal access token for the command line - GitHub Help](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
- [Cloning a repository from GitHub Desktop](https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-desktop)

- [GitHub Desktop | Simple collaboration from your desktop](https://desktop.github.com/)



