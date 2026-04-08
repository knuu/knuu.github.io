# `site-hugo`

Pelican 本体には触れずに Hugo へ段階移行するための独立ワークスペースです。

## 開発

1. Hugo をインストールします。
2. 必要に応じて Pelican 側の原稿から再取り込みします。

```bash
python3 site-hugo/scripts/import_from_pelican.py
```

3. ローカルサーバーを起動します。

```bash
hugo server --source site-hugo
```

4. 本番 build は次で確認できます。

```bash
hugo --source site-hugo --minify
```

## 方針

- 既存の `content/`, `pelicanconf.py`, `output/` は rollback 用の参照元として残します。
- Hugo 側の公開対象は `site-hugo/public/` に限定します。
- `search` と `related posts` は初回移行では戻さず、`/search.html` は案内ページのみ出します。
- GitHub Pages への deploy は repo root の `.github/workflows/hugo-pages.yml` から実行します。
