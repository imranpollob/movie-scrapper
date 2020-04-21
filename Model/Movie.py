# Movie Class/Model
from app import db, ma

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
        


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)