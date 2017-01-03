import fresh_tomatoes
import urllib
import urllib.request
import json
import MovieAPI

url = "https://api.themoviedb.org/3/discover/movie?api_key=c3880d07fc7fcab7025895770629a5bb&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"
json_obj = urllib.request.urlopen(url)
movie_json = json.JSONDecoder(json_obj)
movie_api = json.load(movie_json)
for apimovie in movie_api['results']:
    print (apimovie)