movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# Task 1
def check1(movie):
    return movie["imdb"] > 5.5


# Task 2
def filter_good(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


# Task 3
def filter_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]


# Task 4
def calc_avg_score(movies):
    return sum([movie["imdb"] for movie in movies]) / len(movies)


# Task 5
def calc_avg_score_category(movies, category):
    movies = filter_category(movies, category)
    return calc_avg_score(movies)


print(check1(movies[0]))
print(*filter_good(movies), sep='\n')
print()
print(*filter_category(movies, "Romance"), sep='\n')
print(calc_avg_score(movies))
print(calc_avg_score_category(movies, "Comedy"))
