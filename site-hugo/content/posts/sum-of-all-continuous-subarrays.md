+++
title = "連続する部分列の和の総和"
date = "2018-06-20"
lastmod = "2020-03-02"
slug = "sum-of-all-continuous-subarrays"
url = "/sum-of-all-continuous-subarrays.html"
tags = ["algorithm"]
categories = ["blog"]
authors = ["knuu"]
+++

## 問題

- 長さ $N$ の数列 $A = [a_1, a_2, ..., a_N]$ が与えられる
- この数列の任意の連続する部分列の和の総和を $10^9+7$ で割った余りを求めよ

## 例

$A = [1, 2, 3]$ のとき、和は $1+2+3+(1+2)+(2+3)+(1+2+3)=20$

## 制約

- $1 \le N \le 10^6$
- $-10^9 \le a_i \le 10^9 (i = 1, ..., N)$

## 解法

- $A$ の累積和を取った数列を $S$ とする
    - つまり、$S_i := \sum_{j=1}^{i}a_j$
    - ただし、$S_0 = 0$ とする
- このとき、求める総和は、$\sum_{(i,j):0 \le i < j \le N}(S_j - S_i)$ と書ける
    - $(i,j):0 \le i < j \le N$ は $0 \le i < j \le N$ を満たす組 $(i,j)$ を意味する
- これは和と差しか出てこないため、正の項 $S_j$ と負の項 $-S_i$ がそれぞれ何回この式の中で現れるかを考えればよい
    - 正の項 $S_j(j=0,1,...,N)$ が何回現れるかを考えると、$S_0$ は0回、$S_1$ は 1 回 ($i=0$ のとき)、$S_2$ は 2 回 ($i=0,1$ のとき)、と考えていくと、正の項 $S_j$ は $j$ 回現れる
    - 負の項 $S_i(i=0,...,N-1)$ が何回現れるかを考えると、$S_0$ は $N$ 回 ($j=1,2,...,N$ のとき)、$S_1$ は $N-1$ 回 ($j=2,i...,N$ のとき) と考えていくと、$S_i$ は $(N-i)$ 回現れる
- よって、$\sum_{(i,j):0 \le i < j \le N}(S_j - S_i)=\sum_{i=0}^{N}(i \times S_i - (N-i)\times S_i)=\sum_{i=0}^{N}(2i-N)S_i$ となる
- 以上より、$O(N)$ で問題を解くことができた

## コード

```python
def sum_subarrays(A, mod=10**9+7):
    N = len(A)
    S = [0]
    for a in A:
        S.append(S[-1] + a)
        S[-1] %= mod
    return sum((2 * i - N) * s % mod for i, s in enumerate(S)) % mod
```

- 負の剰余が出てくるが、Python (2/3系ともに) では負の数 $x(x>0)$ の正の数 $m(m>0)$ についての剰余 $x\%m$は$(x+m)\%m$ と一致するため、問題ない
    - C++ ではこのコードは問題が出る
    - 負の数の剰余の計算で負の数が出る場合の計算は、[言語仕様によって異なる](https://shunirr.hatenablog.jp/entry/20120409/1333993409)ため、注意したほうがよい

## 類題

- 連続でなくてよい場合は、総和において各数は $2^{N-1}$ 回出現する
    - よって答えは $2^{N-1}\times\sum_{i=1}^{N}a_i$
- 和ではなく積の場合も同様に求められる
    - $P_0 := 1, P_i := \prod_{j=1}^{i}a_j (i=1,\ldots,N)$ とすると、$\prod_{(i,j):0 \le i < j \le N} \frac{P_j}{P_i}=\prod_{i=0}^{N} \frac{P_i^i}{P_i^{N-i}}=\prod_{i=0}^{N}P_i^{2i-N}$
- 和ではなく bitwise xor の場合も同様で、ビットごとに偶数回か奇数回かを考えればよい
- 連続する部分列の長さが $K$ **以下**という制約がある場合
    - これは正の項 $S_i$、負の項 $-S_i$ が出現する回数が $K$ 回以下という条件だと考えればよいので、答えは $\sum_{i=0}^{N}(\min(i, K) \times S_i - \min(N-i, K)\times S_i)$
- 連続する部分列の長さが $K$ **以上**という制約がある場合
    - $\sum_{i=0}^{N}(\max(i-K+1, 0) \times S_i - \max(N-i-K+1, 0)\times S_i)$

## 参考

[AtCoder Regular Contest 071 - D 井井井 / ###](https://atcoder.jp/contests/arc071/tasks/arc071_b)
