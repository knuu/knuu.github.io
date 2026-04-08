+++
title = "AtCoder で scipy を使って問題を解く"
date = "2021-02-28"
slug = "atcoder-scipy"
url = "/atcoder-scipy.html"
tags = ["competitive_programming"]
categories = ["blog"]
authors = ["knuu"]
+++

AtCoder で scipy を使って解いた問題をメモ代わりに残しておきます．一部 yukicoder や Library-Checker も含まれています（タイトル詐欺）．

AtCoder に入っている numpy / scipy のバージョンはコードテストに以下を入力して実行することで確認できます．

```python
import numpy as np
import scipy as sp
print(f"numpy {np.version.full_version}")
print(f"scipy {sp.version.full_version}")
```

出力結果（2020/02/28 時点）

```
numpy 1.18.2
scipy 1.4.1
```

## グラフアルゴリズム: scipy.sparse.csgraph

### 使うライブラリ

||アルゴリズム・問題|Library Checker|提出|
|---|---|---|---|
|[connected_components](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.connected_components.html)|強連結成分分解（トポロジカルソート）|[問題](https://judge.yosupo.jp/problem/scc)|[Link](https://judge.yosupo.jp/submission/40475)|
|[dijkstra](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html)|単一始点最短路|[問題](https://judge.yosupo.jp/problem/shortest_path)|[Link](https://judge.yosupo.jp/submission/40468)|
|[floyd_warshall](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.floyd_warshall.html)|全点対最短路|-|-|
|[minimum_spanning_tree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.minimum_spanning_tree.html)|最小全域木|-|-|
|[maximum_flow](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_flow.html)|最大フロー|-|-|
|[maximum_bipartite_matching](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_bipartite_matching.html)|二部グラフの最大マッチング|[問題](https://judge.yosupo.jp/problem/bipartitematching)|[Link](https://judge.yosupo.jp/submission/40476)|

### AtCoder 上の問題

||問題|提出|
|---|---|---|
|connected_components|[Educational DP Contest-G Longest Path](https://atcoder.jp/contests/dp/tasks/dp_g)|[Link](https://atcoder.jp/contests/dp/submissions/9852385)|
|dijkstra|[ABC035-D トレジャーハント](https://atcoder.jp/contests/abc035/tasks/abc035_d)|[Link](https://atcoder.jp/contests/abc035/submissions/3859248)|
|dijkstra|[第一回アルゴリズム実技検定-J 地ならし](https://atcoder.jp/contests/past201912-open/tasks/past201912_j)|[Link](https://atcoder.jp/contests/past201912-open/submissions/9260157)|
|floyd_warshall|[ABC143-E Travel by Car](https://atcoder.jp/contests/abc143/tasks/abc143_e)|[Link](https://atcoder.jp/contests/abc143/submissions/9854473)|
|minimum_spanning_tree|[第一回アルゴリズム実技検定-L グラデーション](https://atcoder.jp/contests/past201912-open/tasks/past201912_l)|[Link](https://atcoder.jp/contests/past201912-open/submissions/9236781)|
|maximum_flow|[ABC010-D 浮気予防](https://atcoder.jp/contests/abc010/tasks/abc010_4)|[Link](https://atcoder.jp/contests/abc010/submissions/20563398)|
|maximum_flow|[ABC193-F Zebraness](https://atcoder.jp/contests/abc193/tasks/abc193_f)|[Link](https://atcoder.jp/contests/abc193/submissions/20563184)|
|maximum_bipartite_matching|[ARC092-C 2D Plane 2N Points](https://atcoder.jp/contests/arc092/tasks/arc092_a)|[Link](https://atcoder.jp/contests/arc092/submissions/20563432)|

- 要検証事項等
    - maximum_flow は特殊なケース（source と sink が連結でない場合など）で ValueError が投げられて RuntimeError になることがあるっぽい？

## 最適化: scipy.optimize

### 使うライブラリ

||アルゴリズム・問題|Library Checker|提出|
|---|---|---|---|
|[minimize_scalar](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html)|関数の最小値|-|-|
|[newton](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html)|ニュートン法（関数の根）|-|-|
|[linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)|線形計画法|-|-|
|[linear_sum_assignment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html)|割当問題|[問題](https://judge.yosupo.jp/problem/assignment)|[Link](https://judge.yosupo.jp/submission/40473)|

### AtCoder 上の問題

||問題|提出|
|---|---|---|
|minimize_scalar|[ARC054-B ムーアの法則](https://atcoder.jp/contests/arc054/tasks/arc054_b)|[Link](https://atcoder.jp/contests/arc054/submissions/9856839)|
|minimize_scalar|[ARC049-B 高橋ノルム君](https://atcoder.jp/contests/arc049/tasks/arc049_b)|[Link](https://atcoder.jp/contests/arc049/submissions/9857834)
|newton|[ABC026-D 高橋君ボール1号](https://atcoder.jp/contests/abc026/tasks/abc026_d)|[Link](https://atcoder.jp/contests/abc026/submissions/9853305)|
|linprog|[yukicoder No.453 製薬会社](https://yukicoder.me/problems/no/453)|[Link](https://yukicoder.me/submissions/425071)|

- 要検証事項等
    - linprog を用いる試みは[他にもある](https://kimiyuki.net/writeup/algo/atcoder/arc_050_b/)が，再現しようとしても [Wrong Answer が取れなかった](https://atcoder.jp/contests/arc050/submissions/20563509)

## 計算幾何: scipy.spatial

### 使うライブラリ

||アルゴリズム・問題|Library Checker|提出|
|---|---|---|---|
|[ConvexHull](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html)|凸包|-|-|

### AtCoder 上の問題

||問題|提出|
|---|---|---|
|ConvexHull|[ABC022-D Big Bang](https://atcoder.jp/contests/abc022/tasks/abc022_d)|[Link](https://atcoder.jp/contests/abc022/submissions/9854257)|
|ConvexHull|[AGC021-B Holes](https://atcoder.jp/contests/agc021/tasks/agc021_b)|[Link](https://atcoder.jp/contests/agc021/submissions/9855223)|
|ConvexHull|[yukicoder No.199 星を描こう](https://yukicoder.me/problems/no/199)|[Link](https://yukicoder.me/submissions/345450)|

- 要検討事項
    - ABC022-D を [kd-tree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.html) で最近点対を求める解法でやってみたが，[提出してみると TLE だった](https://atcoder.jp/contests/abc022/submissions/20563595)

## TODO

- FFT
- ボロノイ図・ドロネー三角形分割・KD 木
- from scipy.ndimage import distance_transform_cdt:
    - https://atcoder.jp/contests/agc033/submissions/5279051
    - https://twitter.com/lily0727k/status/1124964133730783233
