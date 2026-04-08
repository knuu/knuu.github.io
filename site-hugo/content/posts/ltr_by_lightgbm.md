+++
title = "LightGBM でかんたん Learning to Rank"
date = "2020-04-05"
slug = "ltr_by_lightgbm"
url = "/ltr_by_lightgbm.html"
tags = ["learning_to_rank", "machine_learning", "information_retrieval"]
categories = ["blog"]
authors = ["knuu"]
+++

## 概要

LightGBM には LambdaRank が実装されており，簡単にランキング学習ができるようになっている．
しかし残念なことに，日本語で試してみた例は非常に少ない．
特に，実際にデータ用意して学習し，評価するところまでやって公開している例がほぼ見当たらない．

そこで，ランキング学習の練習を兼ねて，データの読み込み，モデルの学習，評価までを行う notebook を作成して公開した．
Google Colab で作成しているので，Open in Colab のリンク先に行くことで，作成した notebook を Google Colab 上ですぐに実行することも可能にしている．
データとしては，LightGBM が公式で用意している examples のデータを使用し，評価指標としては NDCG@10 を用いた．

## 作成した notebook

{{< gist "3b978a2d458df5d7910d7e314f9d74f3" >}}

## 参考にさせていただいたの

- [LightGBMでサクッとランク学習やってみる](https://www.szdrblog.info/entry/2018/12/05/001732): examples のデータの形式を参考にさせていただいた
- [LightGBMでランキング学習](https://qiita.com/kondo-k/items/5f1f171da3ac7b98cbcf)
