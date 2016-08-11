# ezgfm

ezgfm は [SimpleHTTPServer] を少し拡張して GitHub 流の Markdown の文書（`*.md`）
が HTML として表示されるようにしたものです。

[SimpleHTTPServer]: http://docs.python.jp/2/library/simplehttpserver.html


## 動作要件

ezgfm は Python 2.x で動作します。また、以下のパッケージが必要です。

~~~~shell
$ pip install markdown py-gfm pygments
~~~~

Note: `pygments` はあったほうがよいですがなくても動作します。


## 使用法

基本的には SimpleHTTPServer と同じです。

~~~~shell
$ python ezgfm.py [PORT]
~~~~

あとはブラウザから http://localhost:8000/ （あるいは指定したポート）にアクセス
してください。

`style.css` がドキュメントルートにあればそれが使われます。


## ライセンス

3-clause BSD License です。全文は [LICENSE.md](LICENSE.md) にあります。
