import requests
import urllib.parse

API_KEY = "490991e1917e06336845e770f051cec8"

query = input("検索: ").strip().replace(" ", "").replace("　", "")
query_encoded = urllib.parse.quote(query)

url = f"https://gnews.io/api/v4/search?q={query_encoded}&lang=ja&country=jp&max=5&apikey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for article in data["articles"]:
        print(f"タイトル:{article['title']}")
        print(f"URL:{article['url']}")
        print(f"サイト名:{article['source']['name']}")
        print("-"*50)
else:
    print(f"APIリクエスト失敗{response.status_code}")
