import requests, random

#API_TOKEN = "api_key=blablabla"



def get_popular_movies():
    endpoint = f"https://api.themoviedb.org/3/movie/popular?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = f"https://image.tmdb.org/t/p/?{API_TOKEN}"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)['results']
    return random.sample(data, k=len(data))[:how_many]


def get_genres():
    endpoint = f"https://api.themoviedb.org/3/genre/tv/list?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()['genres']
    return response


def get_genre_movies(collection_id):
    endpoint = f"https://api.themoviedb.org/3/collection/{collection_id}?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def list_check(list_type):
    genres = get_genres()
    genres = [genres["name"] for genres in genres]
    for genre in genres:
        if list_type == genre:
            return True
        get_movies(how_many=8, list_type="popularr")
    return genres


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?{API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]