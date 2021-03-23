import json
import requests
import os
import urllib.request

config_secret_debug = json.loads(open('settings_debug.json').read())
API_KEY = config_secret_debug['TMDB']['API_KEY']
 
url = "https://api.themoviedb.org/3/movie/top_rated?api_key="+API_KEY+"&language=ko&page="
img_url = "https://image.tmdb.org/t/p/original"

data = []
# 하나에 40개씩 있음 -> 400
for i in range(1, 20):
    request_url = url+str(i)
    request = requests.post(request_url)
    request_json = request.json()
    arr = request_json['results']
    for i in range(len(arr)):
        data.append({
            "pk": i+1,
            "model": "movies.Movie", 
            "fields": {
                'title' : arr[i]['title'],
                'poster_path': img_url+arr[i]['poster_path'],
                'vote_average': round(arr[i]['vote_average']/2, 1),
                'release_date': arr[i]['release_date'],
                'overview': arr[i]['overview'],
                'genres': arr[i]['genre_ids']
            }
        })
with open('Movie.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(data, ensure_ascii=False))
