from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
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
    title = db.Column(db.String(255))
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

    def __init__(self, title, directed_by, produced_by, written_by, starring, music_by, cinematography, edited_by,
                 distributed_by, release_date, running_time, country, language, budget, box_office):
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


# Movie Schema
class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'directed_by', 'produced_by', 'written_by', 'starring', 'music_by', 'cinematography',
                  'edited_by', 'distributed_by', 'release_date', 'running_time', 'country', 'language', 'budget', 'box_office')


# Init schema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# Create a Movie
@app.route('/movie', methods=['POST'])
def add_movie():
    title = request.json['Title']
    directed_by = request.json['Directed by']
    produced_by = request.json['Produced by']
    written_by = request.json['Written by']
    starring = request.json['Starring']
    music_by = request.json['Music by']
    cinematography = request.json['Cinematography']
    edited_by = request.json['Edited by']
    distributed_by = request.json['Distributed by']
    release_date = request.json['Release date']
    running_time = request.json['Running time']
    country = request.json['Country']
    language = request.json['Language']
    budget = request.json['Budget']
    box_office = request.json['Box office']

    new_movie = Movie(title, directed_by, produced_by, written_by, starring, music_by, cinematography, edited_by,
                 distributed_by, release_date, running_time, country, language, budget, box_office)

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
    movie.directed_by = request.json['Directed by']
    movie.produced_by = request.json['Produced by']
    movie.written_by = request.json['Written by']
    movie.starring = request.json['Starring']
    movie.music_by = request.json['Music by']
    movie.cinematography = request.json['Cinematography']
    movie.edited_by = request.json['Edited by']
    movie.distributed_by = request.json['Distributed by']
    movie.release_date = request.json['Release date']
    movie.running_time = request.json['Running time']
    movie.country = request.json['Country']
    movie.language = request.json['Language']
    movie.budget = request.json['Budget']
    movie.box_office = request.json['Box office']

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
        

    new_movie = Movie(title, directed_by, produced_by, written_by, starring, music_by, cinematography, edited_by,
                 distributed_by, release_date, running_time, country, language, budget, box_office)

    db.session.add(new_movie)
    db.session.commit()

    return 'ok'


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
