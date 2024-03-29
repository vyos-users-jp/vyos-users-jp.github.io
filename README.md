vyos-users.jp.github.io
=======================

[![Build Status](https://travis-ci.org/vyos-users-jp/vyos-users-jp.github.io.svg?branch=source)](https://travis-ci.org/vyos-users-jp/vyos-users-jp.github.io)

* [www.vyos-users.jp](http://vyos-users.jp/)のソースおよび設定用リポジトリです。
* [Pelican](http://docs.getpelican.com/)を利用しています。

編集方法
---------------------------------

* 必要な物
    * Python 3.9.x
        * Pelican
        * Markdown

1. ソースコードを取得 `$ git clone --recursive https://github.com/vyos-users-jp/vyos-users-jp.github.io.git`
1. ディレクトリに移動 `$ cd vyos-users-jp.github.io`
1. 必要なパッケージをインストール `$ pip install poetry && poetry install`
1. テーマを取得 `$ git submodule update --init`
1. ページを修正 `$ vi content/pages/index.md` (トップページを修正する場合)
1. 開発用サーバ起動 `$ ./develop_server.sh start 8888`
1. ブラウザで `http://127.0.0.1:8888` を開いて変更内容を確認
1. 修正したソースをリポジトリへコミット&プッシュ `$ git commit -am "index.md追記" && git push`

ライセンス
---------------------------------

[![CC-BY-NC-SA-4.0](http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)
