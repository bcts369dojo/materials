# coding: UTF-8
from graphviz import Digraph

dot = Digraph(format="png", comment='Github Flow')
# dot.attr("node", shape="square", style="filled")

node_start = "作業開始"
node_master_branch = "現在のブランチがmaster\nであることを確認\ngit branch"
node_topic_branch = "work-branch"
node_create_branch = "作業用ブランチ作成\ngit checkout -b work-branch"
node_design = "設計、実装作業"
node_commit = "コミット\ngit add .\ngit commit -m 'comment'"
node_push_remote = "ブランチの作業をプッシュ\n git push -u origin work-branch"
node_if1 = "実装完了？"
node_pull_request = "プルリクエスト"
node_review = "レビュー・相談"
node_merge = "マージ"
node_pull_request_close = "プルリクエストを閉じる"
node_delete_topic_blanch = "作業用ブランチを削除"
node_deploy = "必要があればデプロイ作業"
node_if2 = "レビューOK"
node_end = "終了"

############### ノード

dot.node(node_start, node_start, fontstyle="bold")
dot.node(node_master_branch, node_master_branch, style="filled", color='pink', fontstyle="bold")
dot.node(node_create_branch, node_create_branch, style="filled", color='pink', fontstyle="bold")
dot.node(node_if1, node_if1, shape="diamond", style="rounded,filled", color='orange', fontstyle="bold")
dot.node(node_commit, node_commit, style="filled", color='pink', fontstyle="bold")
dot.node(node_push_remote, node_push_remote, style="filled", color='pink', fontstyle="bold")
dot.node(node_pull_request, node_pull_request, style="filled", color='lightblue', fontstyle="bold")
dot.node(node_review, node_review, style="filled", color='lightblue', fontstyle="bold")
dot.node(node_if2, node_if2, shape="diamond", style="rounded,filled", color='orange', fontstyle="bold")
dot.node(node_pull_request_close, node_pull_request_close, style="filled", color='lightblue', fontstyle="bold")
dot.node(node_merge, node_merge, style="filled", color='lightblue', fontstyle="bold")
dot.node(node_merge, node_merge, style="filled", color='lightblue', fontstyle="bold")
dot.node(node_merge, node_merge, fontstyle="bold")
dot.node(node_delete_topic_blanch, node_delete_topic_blanch, style="filled", color='lightblue', fontstyle="bold")
dot.node(node_end, node_end, fontstyle="bold")

############### エッジ
dot.edge(node_start, node_master_branch, label="", fontsize="10")
dot.edge(node_master_branch, node_create_branch, label="", fontsize="10")
dot.edge(node_create_branch, node_design)
dot.edge(node_design, node_if1)
dot.edge(node_if1, node_commit, label="Yes", fontsize="10")
# dot.edge(node_if1, node_design, label="作業", fontsize="9")
dot.edge(node_commit, node_push_remote)
dot.edge(node_push_remote, node_pull_request)
dot.edge(node_pull_request, node_review)
dot.edge(node_review, node_if2)
dot.edge(node_if2, node_merge, label=" Y", fontsize="10", fontstyle="bold")
dot.edge(node_if2, node_design, label=" N", fontsize="10", fontstyle="bold")
dot.edge(node_merge, node_pull_request_close)
dot.edge(node_pull_request_close, node_delete_topic_blanch)
dot.edge(node_delete_topic_blanch, node_end)

dot.render("simple-github-flow")
