+++
title = "pelican(python3)で日本語のカテゴリやタグごとのページのurlを変更する方法"
date = "2017-10-11"
slug = "pelican-utf8-substitution"
url = "/pelican-utf8-substitution.html"
tags = ["pelican", "python"]
categories = ["blog"]
authors = ["knuu"]
+++

- 動作環境
    - Python 3.6.1
    - pelican 3.7.1

### 状況

pelicanでタグ毎にページを表示するurlは`tag/(タグ名).html`であるが、日本語のタグを付けたときにはurlの(タグ名)の部分がよく分からない文字列に自動変換される。
正確にはアルファベットと数字以外の文字列を使った場合であり、これはカテゴリでも同様である。

例えば、日記というタグが付けられている記事一覧のurlは`tag/ri-ji.html`と変換される。

### 対処

これを直すためには、[公式ドキュメント](http://docs.getpelican.com/en/stable/settings.html)によると、`SLUG_SUBSTITUTIONS`、`AUTHOR_SUBSTITUTIONS`、`CATEGORY_SUBSTITUTIONS`、`TAG_SUBSTITUTIONS`などの設定を`pelicanconf.py`に追加すればよく、以下の例のように置き換え元と置き換え先の文字列の組を記述すれば良い。

```python3
TAG_SUBSTITUTIONS = (('C++', 'cpp'))
```

この場合、`C++`というタグが付けられている記事一覧は、`tag/cpp.html`となる。

しかし日本語タグの場合、同じように書いても上手く行かない。
例えば、

```python3
# 上手くいかない
TAG_SUBSTITUTIONS = (('日記', 'diary'))
```
と設定した場合、日記というタグが付けられている記事一覧のurlは、`tag/diary.html`とはならず、`tag/ri-ji.html`のままとなってしまう。

これを`tag/diary.html`にするには、
```python3
# 上手くいく
from unidecode import unidecode
TAG_SUBSTITUTIONS = ((unidecode('日記'), 'diary'))
```
とすれば直すことができる。

### 原因

ここからは上記のようになる理由である。

アルファベットと数字以外の文字列を使った場合の置き換え操作は[slugify関数](https://github.com/getpelican/pelican/blob/master/pelican/utils.py#L266)が用いられている。
これは`value`(置き換え対象のタグやカテゴリ)と`substitutions`(`pelicanconf.py`で設定した`TAG_SUBSTITUTIONS`など)を引数と取る関数であるが、この関数は`value`を`unidecode.unidecode`で変換した後に、`substitutions`の置き換え元の文字列と`value`を比較して、一致するものがあれば置き換え先の文字列に変換するという動作をしている。

つまり上手くいかなかったの日記のタグの例では、`日記`という文字列を`unidecode.unidecode`で`Ri Ji`に変換してから、substitutions内の`日記`という置き換え下の文字列と比較しているため、日本語タグはどう頑張っても変換されないということが起きていたと考えられる。

なので、`TAG_SUBSTITUTIONS`などで設定を行う時点で、日本語を`unidecode.unidecode`で変換しておけばよい。

### おわりに

python2では検証していないので、もしかしたら違う動作になるかもしれません。
検証をお願いします。
