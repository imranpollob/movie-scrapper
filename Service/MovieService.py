from Model.Movie import *
from sqlalchemy import func

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

    return True



def update_movie_rating(movie):
    movie_from_db = Movie.query.filter(func.lower(Movie.title) == func.lower(movie['title'])). \
        filter(Movie.release_date.contains(movie['release'])).first()

    if movie_from_db:
        print('Updating: ' + movie_from_db.title)
        
        movie_from_db.number_of_ratings = movie['number_of_ratings']
        movie_from_db.ratings = round(sum(movie['ratings']) / len(movie['ratings']), 2)

        db.session.commit()

    return True