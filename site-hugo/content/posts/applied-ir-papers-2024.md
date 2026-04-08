+++
title = "今年読んだ応用検索論文の紹介"
date = "2024-12-22"
slug = "applied-ir-papers-2024"
url = "/applied-ir-papers-2024.html"
tags = ["paper-memo", "information_retrieval"]
categories = ["blog"]
authors = ["knuu"]
+++

この記事は[情報検索・検索技術 Advent Calendar 2024](https://qiita.com/advent-calendar/2024/search) の 22 日目の記事として執筆されました．

## 概要

本記事では，今年読んだ応用検索論文についていくつか紹介をします．応用検索論文というのは本記事の著者が今適当に考えたワードで，主に以下の特徴を持つ傾向にあります．

- 企業の実際の検索システムに組み込まれている
- オフライン評価において，公開データだけでなく，企業内の非公開データも用いられている
- オフライン評価だけでなく，A/B テストなどのオンライン評価も実施され，その結果が載っている
- 論文が学会の Industry Track に相当する Track で採択されている

応用検索論文の良い点と微妙な点を主観で挙げるとすると，以下の通りです．

- 良い点
    - 実際に実システムで適用され，実際に効果が出ている話である<span style="color:gray;"><del>ので上司を説得しやすいかもしれない</del></span>
    - 検索システムにおいて重要なレイテンシの観点に触れられているものも多い（キャッシュの活用など）
    - テックブログ的で読みやすいものが多い
    - 同じ企業の複数の論文を読むことで，その企業の検索システムの発展が垣間見えて面白い
    - アーキテクチャが書いてあることもあり，実際に組み込む際の参考になる（かもしれない）
- 微妙な点
    - 新規性が少なく，人によっては得るものが少ないと感じるかもしれない
    - 形式が [IMRAD](https://ja.wikipedia.org/wiki/IMRAD) っぽくない自由な章立てで書かれていることがあり，普通の論文だと思って読むと，つかみどころがないように感じる部分もある

このように，良い点も微妙な点もあるのですが，検索エンジニアとして実際に組み込むとしたらどうするか？などの妄想が捗ることも多いため，最近はよく応用検索論文を読んでいます．本記事では，今年読んだ応用検索論文として，Facebook，Airbnb，LinkedIn，Spotify，Pinterest，Walmart の論文についてそれぞれ紹介します．それぞれの論文で概要と推しポイントをそれぞれ紹介していきますが，かなり短く紹介するため，もし興味が出た論文については，ぜひ詳細を確認してみてください．

|内容|論文名|
|-|-|
|Facebook の埋め込みベース検索の話|(KDD'20) Embedding-based Retrieval in Facebook Search<br>(KDD'21) Que2Search: Fast and Accurate Query and Document Understanding for Search at Facebook<br>(WebConf'23a) Que2Engage: Embedding-based Retrieval for Relevant and Engaging Products at Facebook Marketplace<br>(WebConf'23b) HierCat: Hierarchical Query Categorization from Weakly Supervised Data at Facebook Marketplace|
|Airbnb の地図検索の話|(KDD'24) Learning to Rank for Maps at Airbnb|
|LinkedIn の属性集合ベースの検索の話|(CIKM'24) Learning Links for Adaptable and Explainable Retrieval|
|Spotify のインスタント検索とクエリサジェストの話|(KDD'21) Neural Instant Search for Music and Podcast<br>(CIKM'23) Graph Learning for Exploratory Query Suggestions in an Instant Search System<br>(SIGIR'24) Bootstrapping Query Suggestions in Spotify's Instant Search Systems|
|Pinterest の埋め込みベース検索の話|(WebConf'24) OmniSearchSage: Multi-Task Multi-Entity Embeddings for Pinterest Search|
|Walmart の埋め込みベース検索の話|(CIKM'24a) Enhancing Relevance of Embedding-based Retrieval at Walmart<br>(KDD'22) Semantic Retrieval at Walmart<br>(CIKM'24b) Relevance Filtering for Embedding-based Retrieval<br>|

## Facebook の埋め込みベース検索の話

概要: Facebook 本体の検索において，埋め込みベース検索（いわゆるベクトル検索）を適用した論文（KDD'20）です．

推しポイント: この論文は，埋め込みベース検索のさきがけとなった論文というイメージ（一番最初の論文ではない）ですが，今まで解説スライドでした内容を知らなかったので，今回改めて読みました．この論文が面白いと感じた点は以下の通りです．

- 研究だと，テキストのみを扱うことが多いが，ユーザ情報や位置情報，一般的な検索システムだと考慮しそうな情報をちゃんと考慮している
- 負例の工夫という，埋め込みベース検索の王道の改善をやってちゃんと効果を挙げている
- 実システムへの適用においても，ただただ適用するだけでなく，効果がありそうなクエリのみに適用するなど，ちゃんと工夫をしている

後続の Facebook Marketplace において埋め込みベース検索を適用した論文（KDD'21，WebConf'23a）もかなり面白かったです．

- Transformer を用いたモデルである XLM を適用しているが，それだけでは不十分で文字 3-gram も必要だったことを実験で明らかにしており，LLM が全てを解決してくれるわけではないことが分かる
- 6.2 節のタイトル `There is no silver bullet for retrieval` がかっこいい
- relevance と engagement の両方が重要であることが分かる

また，Facebook Marketplace のクエリ分類において dual encoder を用いる論文（WebConf'23b）も面白かったです．検索を多クラス分類として解く話は extreme classification の文脈で以前よく Amazon が研究していましたが，この論文はその逆で多クラス分類に検索の技術（dual encoder）を使っており，なるほど！となりました．

|||
|-|-|
|KDD'20|[Embedding-based Retrieval in Facebook Search](https://research.facebook.com/publications/embedding-based-retrieval-in-facebook-search/)|
|KDD'21|[Que2Search: Fast and Accurate Query and Document Understanding for Search at Facebook](https://research.facebook.com/publications/que2search-fast-and-accurate-query-and-document-understanding-for-search-at-facebook/)|
|WebConf'23a|[Que2Engage: Embedding-based Retrieval for Relevant and Engaging Products at Facebook Marketplace](https://research.facebook.com/publications/que2engage-embedding-based-retrieval-for-relevant-and-engaging-products-at-facebook-marketplace/)|
|WebConf'23b|[HierCat: Hierarchical Query Categorization from Weakly Supervised Data at Facebook Marketplace](https://research.facebook.com/publications/hiercat-hierarchical-query-categorization-from-weakly-supervised-data-at-facebook-marketplace/)|

## Airbnb の地図検索の話

概要: Airbnb の地図検索において，ランキングと UI を繰り返し改善していく論文（KDD'24）です．詳しくは[別の記事](/kdd24-airbnb-map.html)で解説しているため，そちらをご覧ください．

推しポイント: 通常の検索改善においては，主にランキング（並び順）の改善に着目がいくことが多いですが，これは主にリスト表示を仮定したものが多いです．一方で地図表示においては，リスト表示では成り立つ「ユーザは，ランキングの上位から順にアイテム（宿）を見る」という単純な仮定が成り立ちません．そこに着目し，様々な改善を実施していき，着実に効果を出している点が面白かったです．

|||
|-|-|
|KDD'24|[Learning to Rank for Maps at Airbnb](https://arxiv.org/abs/2407.00091)|

## LinkedIn の属性集合ベースの検索の話

概要: LinkedIn の検索において，ユーザの属性集合と求人の属性集合の間のリンクを学習し，それを求人検索/推薦の第 1 段階の検索に利用するという論文（CIKM'24）です．これにより，求人クリック数が約 31% 増加するなど，各種指標が改善したそうです．

推しポイント: この論文が面白いと感じた点として，大規模にルールを学習しているという点です．ベクトル検索とは違って，ルールなので解釈性が比較的高く，かつ加えたいルールの追加や，不要なルールの削除などが比較的容易にしやすいため，運用が比較的やりやすそうな点が良いと思いました．LLM でベクトル検索するのが流行っているこの時代においても，説明性や運用のしやすさが求められるドメインはあるはずなので，このような方法もあることを知っておくとどこかで使えそうな気がします．

|||
|-|-|
|CIKM'24|[Learning Links for Adaptable and Explainable Retrieval](https://dl.acm.org/doi/10.1145/3627673.3679953)|

## Spotify のインスタント検索とクエリサジェストの話

概要: Spotify におけるインスタント検索において，Transformer ベースのモデルを用いる論文（KDD'21）です．インスタント検索とは，ユーザが入力するたびに検索結果を表示するタイプの検索です．似た機能として，クエリ候補を出すクエリ自動補完がありますが，クエリ自動補完とは違って，インスタント検索ではユーザ入力検索対象のアイテムを直接出します．

推しポイント: この論文の面白い点として，テキストに対しては Transformer ベースのモデルを使っていますが，それだけでは不十分なので，アイテム埋め込みも使っている点です．インスタント検索における有効な手法として，クエリ自動補完でも使われている Most Popular Completion（MPC）的な手法があります．テキストだけを扱う Transformer ベースの手法では，MPC のような人気度を考慮できないので，それを考慮して別途学習したアイテム埋め込みを用いるというのは，確かに，となりました．

その他にも Spotify から出ている論文として，探索的検索（exploratory search）を支援するために，多様性を考慮した node2vec ベースのクエリ推薦を行う論文など，クエリ推薦系の論文（CIKM'23，SIGIR'24）が面白かったです．

|||
|-|-|
|KDD'21|[Neural Instant Search for Music and Podcast](https://mounia-lalmas.blog/wp-content/uploads/2021/07/kdd2021.pdf)|
|CIKM'23|[Graph Learning for Exploratory Query Suggestions in an Instant Search System](https://mounia-lalmas.blog/wp-content/uploads/2023/11/cikmgraphlearning.pdf)|
|SIGIR'24|[Bootstrapping Query Suggestions in Spotify's Instant Search Systems](https://dl.acm.org/doi/10.1145/3539618.3591827)|

## Pinterest の埋め込みベース検索の話

概要: Pinterest の複数の検索タスクを同時に，同じクエリエンコーダで学習することで，埋め込みベースの検索を複数の検索システムで実現しつつ，機械学習モデルを管理するコストを減らしたという論文です．[以前のテックブログ](https://medium.com/pinterest-engineering/searchsage-learning-search-query-representations-at-pinterest-654f2bb887fc)の続編となる論文でもあります．

推しポイント: `3.6 Model Serving` が個人的にはかなり面白いと感じました．埋め込みベースの検索においては，文書側は事前にインデックス時に埋め込みを作成できますが，クエリ側は検索時に埋め込みを作成する必要があります．ただ，Pinterest の検索システムにおいては，秒間 30 万回クエリが来るため，毎回埋め込みを作成していては到底間に合いません．そこでキャッシュを活用し，TTL をチューニングすることで，実際にクエリ時に推論するクエリを秒間 500 回にまで下げることに成功しています．Pinterest の QPS の多さ自体も驚きですが，キャッシュなどの工夫次第で，実際に推論が必要なクエリの QPS をここまで下げられることに驚きました．

|||
|-|-|
|WebConf'24|[OmniSearchSage: Multi-Task Multi-Entity Embeddings for Pinterest Search](https://dl.acm.org/doi/10.1145/3589335.3648309)|

## Walmart の埋め込みベース検索の話

概要: Walmart の埋め込みベースの検索を改善した論文（CIKM'24a）です．Walmart は 2 年前に，埋め込みベース検索を導入した論文を発表していました（KDD'22）が，ログのノイズや，負例の偽陰性，typo の扱いなどに問題がありました．本論文ではこれらの問題を改善する手法をそれぞれ導入し，オンライン実験（A/B テスト）において，適合性（nDCG）やエンゲージメント（売上）を統計的有意に改善しました．

推しポイント: ログから得られるエンゲージメントベースのラベルと，人力で得る適合性のラベルをうまく連携させているように思えた点です．通常，これら 2 つのラベルは別々に扱うことが多い認識ですが，この論文では，適合性報酬モデル（Relevance Reward Model）と題して，人力の適合性のラベルで学習したモデルでエンゲージメントベースのラベルを修正するなど，ログのラベルと人力のラベルの両方をうまく連携して活用することで，指標を改善している点が面白いと思いました．

それ以外にも，再現率が重視されがちな埋め込みベース検索に対して，クエリ依存の閾値で足切りをすることで，精度面の改善をする論文（CIKM'24b）も面白かったです．検索勉強会でも [Vespa でスコアの足切りをする話](https://speakerdeck.com/szdr/vespawoli-yong-sitatekuibekutorujian-suo?slide=6)があったり，検索拡張生成（RAG）の文脈で，[Dropbox のブログ](https://dropbox.tech/machine-learning/bringing-ai-powered-answers-and-summaries-to-file-previews-on-the-web)でも似たような話があったりするなど，実応用でも気になる人が多いトピックなため，気になる人は多い気がします．

|||
|-|-|
|CIKM'24a|[Enhancing Relevance of Embedding-based Retrieval at Walmart](https://arxiv.org/abs/2408.04884)|
|KDD'22|[Semantic Retrieval at Walmart](https://arxiv.org/abs/2412.04637)|
|CIKM'24b|[Relevance Filtering for Embedding-based Retrieval](https://arxiv.org/abs/2408.04887)|

## おわりに

本記事では，著者が今年読んだ応用検索論文を紹介しました．
まだまだ読みたいと考えている応用検索論文が積んであるので，引き続き読んでいきたいです．

また，このテックブログバージョンもどこかで書きたいと思って貯めているので，ご期待ください．

みなさんもぜひ応用検索論文を読んで紹介しましょう！！！
