from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Movie Class/Model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    directed_by = db.Column(db.String(255))
    produced_by = db.Column(db.String(255))
    written_by = db.Column(db.String(255))
    starring = db.Column(db.String(255))
    music_by = db.Column(db.String(255))
    cinematography = db.Column(db.String(255))
    edited_by = db.Column(db.String(255))
    distributed_by = db.Column(db.String(255))
    release_date = db.Column(db.String(255))
    running_time = db.Column(db.String(255))
    country = db.Column(db.String(255))
    language = db.Column(db.String(255))
    budget = db.Column(db.String(255))
    box_office = db.Column(db.String(255))
    number_of_ratings = db.Column(db.Integer)
    ratings = db.Column(db.Float)

    def __init__(self, title, directed_by, produced_by, written_by, starring, music_by, cinematography, edited_by,
                 distributed_by, release_date, running_time, country, language, budget, box_office, number_of_ratings, ratings):
        self.title = title
        self.directed_by = directed_by
        self.produced_by = produced_by
        self.written_by = written_by
        self.starring = starring
        self.music_by = music_by
        self.cinematography = cinematography
        self.edited_by = edited_by
        self.distributed_by = distributed_by
        self.release_date = release_date
        self.running_time = running_time
        self.country = country
        self.language = language
        self.budget = budget
        self.box_office = box_office
        self.number_of_ratings = number_of_ratings
        self.ratings = ratings


# Movie Schema
class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'directed_by', 'produced_by', 'written_by', 'starring', 'music_by', 'cinematography',
                  'edited_by', 'distributed_by', 'release_date', 'running_time', 'country', 'language', 'budget',
                  'box_office', 'number_of_ratings', 'ratings')


# Init schema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# Check value
def check(request, key):
    return request.json[key] if key in request.json else None

# Create a Movie
@app.route('/movie', methods=['POST'])
def add_movie():
    title = request.json['Title']
    directed_by = check(request,'Directed by')
    produced_by = check(request,'Produced by')
    written_by = check(request,'Written by')
    starring = check(request,'Starring')
    music_by = check(request,'Music by')
    cinematography = check(request,'Cinematography')
    edited_by = check(request,'Edited by')
    distributed_by = check(request,'Distributed by')
    release_date = check(request,'Release date')
    running_time = check(request,'Running time')
    country = check(request,'Country')
    language = check(request,'Language')
    budget = check(request,'Budget')
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
    per_page = int(request.args.get('count')) if request.args.get('count') else 20
    all_movies = Movie.query.paginate(page, per_page, False).items  #.all()
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


# Add movie from scrapping
def add_movie_from_scrape(movie = {}):
    title = movie['Title']
    directed_by = movie['Directed by']
    produced_by = movie['Produced by']
    written_by = movie['Written by']
    starring = movie['Starring']
    music_by = movie['Music by']
    cinematography = movie['Cinematography']
    edited_by = movie['Edited by']
    distributed_by = movie['Distributed by']
    release_date = movie['Release date']
    running_time = movie['Running time']
    country = movie['Country']
    language = movie['Language']
    budget = movie['Budget']
    box_office = movie['Box office']
    number_of_ratings = movie['number_of_ratings']
    ratings = movie['ratings']
        

    new_movie = Movie(title, directed_by, produced_by, written_by, starring, music_by, cinematography, edited_by,
                 distributed_by, release_date, running_time, country, language, budget, box_office, number_of_ratings, ratings)

    db.session.add(new_movie)
    db.session.commit()

    return 'saved'



def update_movie_rating(movie):
    movie_from_db = Movie.query.filter(func.lower(Movie.title) == func.lower(movie['title'])). \
        filter(Movie.release_date.contains(movie['release'])).first()

    if movie_from_db:
        print('Updating: ' + movie_from_db.title)
        
        movie_from_db.number_of_ratings = movie['number_of_ratings']
        movie_from_db.ratings = round(sum(movie['ratings']) / len(movie['ratings']), 2)

        db.session.commit()

    return 'updated'


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
