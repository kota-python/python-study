# Yahooニュース ランキング記事スクレイピングツール

このリポジトリでは、Yahooニュースのアクセスランキングページから注目記事のタイトルとURLを取得するWebスクレイピングスクリプトを公開しています。  
Pythonの基本文法に加えて、`requests`、`BeautifulSoup`、`re`（正規表現）といったライブラリを活用して、ニュース記事の情報を自動抽出しています。

---

## 概要

- 対象サイト: [Yahoo!ニュース アクセスランキング](https://news.yahoo.co.jp/ranking/access/news)
- 抽出内容: 記事タイトル、記事URL
- 使用ライブラリ:
  - `requests`: Webページの取得
  - `BeautifulSoup`: HTMLパース
  - `re`: 記事リンクの抽出（正規表現）

---

## 学習ポイント・工夫

- **HTML構造の解析**を行い、ニュース記事だけを対象に抽出するように条件を設定
- **正規表現**を用いて、`"news.yahoo.co.jp/articles"` を含むリンクのみを判別
- `BeautifulSoup` の `get_text(strip=True)` を使って無駄な空白を除去し、記事タイトルをきれいに取得

---

## 実行方法

```bash
python web_scraping_yahoo.py
```

---

## 実行例

```
検索: ○○
タイトル: ○○
URL: https://example.com/article123
サイト名: ○○
--------------------------------------------------
```
---

## 使用環境

- python3.13.5
- 開発環境:Visual Studio Code（Windows）
