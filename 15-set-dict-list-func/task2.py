def best_movies(films):
    max_rating = None
    for movie in films:
        if max_rating is None:
            max_rating = movie
        else:
            if movie['rating'] > max_rating['rating']:
                max_rating = movie

    return f"Name: {max_rating['title']}\nRating: {max_rating['rating']} "



movies = [
    {"title": "The Shawshank Redemption", "rating": 9.3},
    {"title": "The Godfather", "rating": 9.2},
    {"title": "The Dark Knight", "rating": 9.0},
    {"title": "12 Angry Men", "rating": 9.0},
    {"title": "Schindler's List", "rating": 8.5},
    {"title": "The Lord of the Rings: The Return of the King", "rating": 9.8},
    {"title": "Pulp Fiction", "rating": 8.9},
    {"title": "The Good, the Bad and the Ugly", "rating": 8.8},
    {"title": "Forrest Gump", "rating": 8.8},
    {"title": "Inception", "rating": 8.8}
]

print(best_movies(movies))