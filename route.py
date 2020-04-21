from flask import request, jsonify
from app import app
from Model.Movie import *

# Check value
def check(request, key):
    return request.json[key] if key in request.json else None


# Create a Movie
@app.route('/movie', methods=['POST'])
def add_movie():
    title = request.json['Title']
    directed_by = check(request, 'Directed by')
    produced_by = check(request, 'Produced by')
    written_by = check(request, 'Written by')
    starring = check(request, 'Starring')
    music_by = check(request, 'Music by')
    cinematography = check(request, 'Cinematography')
    edited_by = check(request, 'Edited by')
    distributed_by = check(request, 'Distributed by')
    release_date = check(request, 'Release date')
    running_time = check(request, 'Running time')
    country = check(request, 'Country')
    language = check(request, 'Language')
    budget = check(request, 'Budget')
    box_office = check(request, 'Box office')
    number_of_ratings = check(request, 'number_of_ratings')
    ratings = check(request, 'ratings')

    new_movie = Movie(title, directed_by, produced_by, written_by, starring, music_by, cinematography, edited_by,
                      distributed_by, release_date, running_time, country, language, budget, box_office, number_of_ratings, ratings)

    db.session.add(new_movie)
    db.session.commit()

    return movie_schema.jsonify(new_movie)


# Get All Movies
@app.route('/movies', methods=['GET'])
def get_movies():
    page = int(request.args.get('page')) if request.args.get('page') else 1
    per_page = int(request.args.get('count')
                   ) if request.args.get('count') else 20
    all_movies = Movie.query.paginate(page, per_page, False).items  # .all()
    return jsonify(movies_schema.dump(all_movies))


# Search Movies
@app.route('/movies/search/<title>', methods=['GET'])
def search_movies(title):
    all_movies = Movie.query.filter(Movie.title.like('%' + title + '%')).all()
    return jsonify(movies_schema.dump(all_movies))


# Get Single Movies
@app.route('/movie/<id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    return movie_schema.jsonify(movie)


# Update a Movie
@app.route('/movie/<id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)

    movie.title = request.json['Title']
    movie.directed_by = check(request, 'Directed by')
    movie.produced_by = check(request, 'Produced by')
    movie.written_by = check(request, 'Written by')
    movie.starring = check(request, 'Starring')
    movie.music_by = check(request, 'Music by')
    movie.cinematography = check(request, 'Cinematography')
    movie.edited_by = check(request, 'Edited by')
    movie.distributed_by = check(request, 'Distributed by')
    movie.release_date = check(request, 'Release date')
    movie.running_time = check(request, 'Running time')
    movie.country = check(request, 'Country')
    movie.language = check(request, 'Language')
    movie.budget = check(request, 'Budget')
    movie.box_office = check(request, 'Box office')

    if check(request, 'number_of_ratings'):
        movie.number_of_ratings = check(request, 'number_of_ratings')

    if check(request, 'ratings'):
        movie.ratings = check(request, 'ratings')

    db.session.commit()

    return movie_schema.jsonify(movie)


# Delete Movie
@app.route('/movie/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    return movie_schema.jsonify(movie)
