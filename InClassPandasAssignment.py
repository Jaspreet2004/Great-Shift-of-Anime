
import requests
import pandas as pd
import time

CLIENT_ID = "05c9f985c6e952bb896b822d18d0364f"
headers = {"X-MAL-CLIENT-ID": CLIENT_ID}

search_url = "https://api.myanimelist.net/v2/anime"

queries = ["action", "romance", "fantasy", "sports", "comedy", "drama"]
anime_ids = set()
rows = []

MAX_IDS = 50

# Step 1: collect anime IDs
for q in queries:
    print(f"Searching for query: {q}")

    params = {
        "q": q,
        "limit": 50
    }

    try:
        response = requests.get(search_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        print(f"Timeout while searching for query: {q}")
        continue
    except requests.exceptions.RequestException as e:
        print(f"Request failed for query '{q}': {e}")
        continue

    for anime in data.get("data", []):
        anime_ids.add(anime["node"]["id"])
        if len(anime_ids) >= MAX_IDS:
            break

    print(f"IDs collected so far: {len(anime_ids)}")

    if len(anime_ids) >= MAX_IDS:
        break

    time.sleep(0.3)

print(f"\nTotal IDs collected: {len(anime_ids)}")

# Step 2: fetch details for each anime
for i, anime_id in enumerate(anime_ids, start=1):
    print(f"{i}/{len(anime_ids)} -> Fetching anime ID: {anime_id}")

    detail_url = f"https://api.myanimelist.net/v2/anime/{anime_id}"
    params = {
        "fields": "id,title,mean,rank,popularity,num_episodes,start_date,end_date,synopsis,media_type,genres,studios,source,start_season"
    }

    try:
        response = requests.get(detail_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        node = response.json()
    except requests.exceptions.Timeout:
        print(f"Timeout for anime ID: {anime_id}")
        continue
    except requests.exceptions.RequestException as e:
        print(f"Error for anime ID {anime_id}: {e}")
        continue

    start_date = node.get("start_date")
    end_date = node.get("end_date")
    year = start_date[:4] if start_date else None

    rows.append({
        "id": node.get("id"),
        "title": node.get("title"),
        "episodes": node.get("num_episodes"),
        "rating": node.get("mean"),
        "rank": node.get("rank"),
        "popularity": node.get("popularity"),
        "start_date": start_date,
        "end_date": end_date,
        "year": year,
        "synopsis": node.get("synopsis"),
        "media_type": node.get("media_type"),
        "genres_raw": str(node.get("genres", [])),
        "studios_raw": str(node.get("studios", [])),
        "source": node.get("source")
    })

    time.sleep(0.3)

# Step 3: raw messy dataset
df = pd.DataFrame(rows)

df.to_csv("mal_anime_raw_messy.csv", index=False)

print("\nFirst 5 rows of messy data:")
print(df.head())

print("\nRows collected:", len(df))
print("\nSaved file: mal_anime_raw_messy.csv")