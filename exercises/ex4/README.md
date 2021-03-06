# Github Labels

## はじめに

一般的に、課題（Issue）を起票する場合には、適切なラベルをつけます。

Issueは質問の他、作業予定内容、通達、議論など多くのことで利用するため、ラベルが付与されていないと、そのIssueが何の目的のものなのかをすぐに理解できません。
ラベルの付与の仕方、ラベルの作り方について学習してください。

なお、ラベルはIssueのほか、プルリクエストにも付与することができますが、管理と理解が煩雑になるため、本道場ではラベルはIssueだけに付与することを推奨します。


参考情報を一読し、理解度チェックをに進んでください。


## 理解度チェック

### シナリオ

担当者:生徒の皆さん、レビュワー:bcts369となります。

今回の課題では、発生したバグを修正する作業のIssueを起票することを想定し、次のことを行ってください。

> **既存の**自己紹介用の設定ファイル（profile.toml）の内容に次の項目を追加して、自分の情報を指定してください。

```
learning-status = "Exercise4"
```

- ラベル名を `bug` から `バグ` に変更してください。
- 自分で課題を起票してください（タイトル、コメント）
- Issueの右メニューでAssignees（担当）を指定してください（自分にする）
- Issueの右メニューで、変更した **バグ** ラベルを選択してください。
- 作業対象リポジトリは、生徒各自が作成した`bcts369dojo`です。
- `master`ブランチから作業用のブランチを作って作業を開始してください。
- コミット時には、Issue番号を先頭に書いてください。 例）git commit -m '#4 作業内容'
- 作業が完了したら、プルリクエストしてください（右メニューでReviewerとAssigneesを指定してください）。

プルリクエストをしていただいた後に、私が指示通りに行われたかどうかをレビューし、結果を伝えます。


OKの場合は、`master`ブランチにマージしてください。

マージが問題なく完了したら、後処理として、プルリクエストを終了し、作業用に作ったブランチは削除してください。


## 参考情報へのリンク

### Official

- [About labels - GitHub Help](https://help.github.com/en/articles/about-labels)
- [Creating a label - GitHub Help](https://help.github.com/en/articles/creating-a-label)

