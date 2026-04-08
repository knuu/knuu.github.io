+++
title = "確率分布早見表"
date = "2017-06-18"
slug = "probability-distributions"
url = "/probability-distributions.html"
tags = ["statistics"]
categories = ["blog"]
authors = ["knuu"]
+++

## 離散分布

|確率分布|確率密度関数|定義域|パラメータ|平均|分散|
|:-:|:-:|:-:|:-:|:-:|:-:|
|ベルヌーイ分布|$p^x (1-p)^{1-x}$|$x\in \{0,1\}$|$p$|$p$|$p(1-p)$|
|二項分布|${}_nC_xp^x(1-p)^{n-x}$|$x\in \{0,\cdots,n\}$|$n,p$|$np$|$np(1-p)$|
|ポアソン分布|$\frac{\lambda^xe^{-\lambda}}{x!}$|$x\in \{0,1,\cdots\}$|$\lambda$|$\lambda$|$\lambda$|
|幾何分布|$p(1-p)^{x-1}$|$x\in \{1,2,\cdots\}$|$p$|$\frac{1}{p}$|$\frac{1-p}{p^2}$|
|(離散)一様分布|$\frac{1}{N}$|$x\in \{1,\cdots,N\}$|$N$|$\frac{N+1}{2}$|$\frac{N^2-1}{12}$|

## 連続分布

|確率分布|確率密度関数|定義域|パラメータ|平均|分散|
|:-:|:-:|:-:|:-:|:-:|:-:|
|正規分布|$\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$|$(-\infty,\infty)$|$\mu,\sigma$|$\mu$|$\sigma^2$|
|指数分布|$\lambda e^{-\lambda x}$|$[0,\infty)$|$\lambda$|$\frac{1}{\lambda}$|$\frac{1}{\lambda^2}$|
|(連続)一様分布|$\frac{1}{b-a}$|$[a,b]$|$a,b$|$\frac{a+b}{2}$|$\frac{(a-b)^2}{12}$|
