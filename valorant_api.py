import requests
import json

# API_KEYは 'https://developer.riotgames.com/' で取得できるので随時変更する．
API_KEY = "RGAPI-6cd59469-1adf-45ed-b837-246807d06779"

name = "okokp"
region = "jp"
url = f"https://ap.api.riotgames.com/val/content/v1/contents?locale=ja-JP&api_key=RGAPI-445df9c3-9d1b-47bb-a0e0-48f9ca243992"


# APIリクエスト
response = requests.get(url)
if response.status_code == 200:
    valorant_data = response.json()

    # エージェント
    characters = valorant_data.get("characters", [])
    agent_names = [agent["name"] for agent in characters]
    print(agent_names)
    # 出力例: ["ゲッコー", "フェイド", "ブリーチ", ...]

    # マップ
    maps = valorant_data.get("maps", [])
    map_names = [map_data["name"] for map_data in maps if "assetPath" in map_data]
    print(map_names)
    # 出力例: ["アセント", "スプリット", "フラクチャー", ...]

    # プレイヤータイトル
    player_titles = valorant_data.get("playerTitles", [])
    titles_name = [
        titles["name"].replace("タイトル", "").strip() for titles in player_titles
    ]
    print(titles_name)

else:
    print(f"API request failed with status code: {response.status_code}")
