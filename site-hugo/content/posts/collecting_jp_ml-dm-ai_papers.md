+++
title = "機械学習・データマイニング・人工知能分野周りの日本所属の国際会議論文を集めてみる"
date = "2019-08-12"
slug = "collecting_jp_ml-dm-ai_papers"
url = "/collecting_jp_ml-dm-ai_papers.html"
tags = ["scraping"]
categories = ["blog"]
authors = ["knuu"]
+++

## 概要

学生が研究室を選んだり、企業が共同研究先を選ぶ際に、その研究室がきちんと論文を通している研究室かどうかというのは一つに基準になるかと思います。計算機科学分野、特に機械学習・データマイニング・人工知能分野周りの分野では、企業の研究所が強く速報性が求められる影響などにより国際会議論文の影響力が強い傾向があります。そこで本記事では、これらの分野の国際会議に日本所属で論文を通している人を収集することを考えます。

本記事では機械学習・データマイニング・人工知能分野の国際会議を [ML, DM, and AI Conference Map](http://www.kamishima.net/archive/MLDMAImap.pdf) に記載されている国際会議とします。

## 手法

日本所属の国際会議論文を収集する方法として、現在は目視で収集する方法が主流です。既存のプロジェクトとしては以下のものがあります。

- [SIGGRAPH Papers by Japanese Researchers](https://siggraph.xyz/japanese/)
- [IEEE Journals & Magazines - papers published by researchers in Japan](https://ishikawa.cc/ieee/index.html)
- [日本所属の言語処理トップカンファレンス論文](http://murawaki.org/misc/japan-nlp-2018.html)
- [情報検索を研究している日本の研究室一覧](https://medium.com/@mpkato/%E6%83%85%E5%A0%B1%E6%A4%9C%E7%B4%A2%E3%82%92%E7%A0%94%E7%A9%B6%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E6%97%A5%E6%9C%AC%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E4%B8%80%E8%A6%A7-7e4961054c7e)

目視で収集する手法の問題点として、スケールしないことがあげられます。さらに近年は機械学習・データマイニング・人工知能分野の国際会議論文は増加している傾向もあり、目視で収集するには限界があります。

そこで今回は [ACM Digital Library](https://dl.acm.org) (ACM DL) のような、各学会や企業が公開している Digital Library の情報を利用して自動で収集することを考えます。Digital Library にはその学会が主催する国際会議やジャーナル論文が登録されており、著者の所属組織とその所在地が記載されています。

- [ACM DL における論文の例](https://dl.acm.org/citation.cfm?doid=3331184.3331220)

![論文の例](/images/acmdl_example.png)

Digital Library を利用することで、どの国のどの組織に所属しているかを容易に収集することができるようになるという利点もありますが、別々の国の組織に複数所属している場合でも 1 つの国に所属している扱いになるなど、目視に比べて正確さに欠けるという欠点もあります（今回はこの部分には目を瞑ります）。

収集は以下の手順で行います。

1. dblp の該当会議の該当年のページにアクセスし、論文名・著者名・Digital Library へのリンクを収集する
2. 論文ごとに収集した Digital Library のリンクをたどり、遷移先のページの著者情報を収集する

上記の手順により、まず、ACM DL を対象として、KDD, CIKM, SIGMOD, PODS, SIGIR, WWW, WSDM, RecSys, STOC について、2016 年から 2019 年の論文を収集しました（ただし CIKM, RecSys は 2019 年は未開催のためありません）。

### SIGMOD のデータ例

注: SIGMOD はデータベース分野のトップカンファレンスです。

| 年   | タイトル                                                     | 著者                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2016 | Local Similarity Search for Unstructured Text                | Pei Wang(名大)<br/>Chuan Xiao(名大)<br/>Jianbin Qin(The University of New South Wales)<br/>Wei Wang(The University of New South Wales)<br/>Xiaoyang Zhang(The University of New South Wales)<br/>Yoshiharu Ishikawa(名大) |
| 2017 | Landmark Indexing for Evaluation of Label-Constrained Reachability Queries | Lucien D.J. Valstar(Eindhoven University of Technology)<br/>George H.L. Fletcher(Eindhoven University of Technology)<br/>Yuichi Yoshida(NII; PFI) |
| 2017 | Coarsening Massive Influence Networks for Scalable Diffusion Analysis | Naoto Ohsaka(東大; JST)<br/>Tomohiro Sonobe(NII; JST)<br/>Sumio Fujita(Yahoo Japan)<br/>Ken-ichi Kawarabayashi(NII; JST) |
| 2017 | Cryptanalysis of Comparable Encryption in SIGMOD'16          | Caleb Horst(University of Washington Tacoma)<br/>Ryo Kikuchi(NTT)<br/>Keita Xagawa(NTT) |
| 2017 | Scaling Locally Linear Embedding                             | Yasuhiro Fujiwara(NTT)<br/>Naoki Marumo(NTT)<br/>Mathieu Blondel(NTT)<br/>Koh Takeuchi(NTT)<br/>Hideaki Kim(NTT)<br/>Tomoharu Iwata(NTT)<br/>Naonori Ueda(NTT) |
| 2017 | QUILTS: Multidimensional Data Partitioning Framework Based on Query-Aware and Skew-Tolerant Space-Filling Curves | Shoji Nishimura(NEC)<br/>Haruo Yokota(東工大)                |
| 2018 | Managing Non-Volatile Memory in Database Systems             | Alexander van Renen(Technische Universität München)<br/>Viktor Leis(Technische Universität München)<br/>Alfons Kemper(Technische Universität München)<br/>Thomas Neumann(Technische Universität München)<br/>Takushi Hashida(富士通研究所)<br/>Kazuichi Oe(富士通研究所)<br/>Yoshiyasu Doi(富士通研究所)<br/>Lilian Harada(富士通研究所)<br/>Mitsuru Sato(富士通研究所) |
| 2019 | Autocompletion for Prefix-Abbreviated Input                  | Sheng Hu(名大; 京大)<br/>Chuan Xiao(名大; 阪大)<br/>Jianbin Qin(Shenzhen University)<br/>Yoshiharu Ishikawa(名大)<br/>Qiang Ma(京大) |

収集したデータは順次以下のページに掲載予定です。

[ML-DM-AI Papers by Researchers in Japan](/pages/ml-dm-ai_jp_papers.html)

## 今後の方針について

最終的な目標としては、[ML, DM, and AI Conference Map](http://www.kamishima.net/archive/MLDMAImap.pdf) にある国際会議について全て収集することを考えています。

この中でも、IEEE Xplore や SpringerLink に登録されている論文については同様に集めることが可能です。ただ、IEEE Xplore については所属組織が登録されていない場合も多くあります。また、Neurips/ICML/COLT のような機械学習系や、ACL/EMNLP/NAACL などの自然言語処理系の国際会議については、Digital Library に登録されていないため、この手法で集めることができません。そこで、以下の方法を考えています。

- PDF を収集し、parse する
    - 使えそうなツール
        - https://github.com/allenai/spv2
        - https://github.com/WING-NUS/Neural-ParsCit
- 著者の他の論文の情報を使う
    - 著者の dblp のリンクをたどり、Digital Library へのリンクがある論文を探す

他にやり方がありましたら、ぜひ twitter で [@n_knuu6](https://twitter.com/n_knuu6) までお教えいただけますと幸いです。
