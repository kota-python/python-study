import requests
from bs4 import BeautifulSoup
import re

# アクセスランキングページのURL
url = "https://news.yahoo.co.jp/ranking/access/news"

# URLにアクセスしてHTMLを取得
res = requests.get(url)

# 取得したHTMLをパース（解析）する
soup = BeautifulSoup(res.content, "html.parser")

# ページ内のすべての<a>タグ（リンク）を取得
elems = soup.find_all("a", href=True)

# 記事リンク（"articles" を含むURL）のみを抽出して出力
for elem in elems:
    href = elem["href"]

    if re.search("news.yahoo.co.jp/articles", href):
        print(f"記事タイトル: {elem.get_text(strip=True)}")
        print(f"記事URL: {href}")
        print("ーーーーーーーーーーーーーーーーーーーーーーー")
