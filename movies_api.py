import fresh_tomatoes
import requests
import json
import MovieAPI
import movies

url = "https://api.themoviedb.org/3/discover/movie?api_key=c3880d07fc7fcab7025895770629a5bb&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"
r = requests.get(url)
json_obj = r.json()
movie_list_api = []

for movie in json_obj["results"]:
  api_title = movie['title']
  api_storyline = movie['overview']
  api_rating = movie['vote_average']
  movieItem = MovieAPI.MovieAPI(api_title, api_storyline, api_rating)
  movie_list_api.append(movieItem)
 
print(movie_list_api)
