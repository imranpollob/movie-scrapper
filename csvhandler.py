import requests
import csv
import re
from Service.MovieService import update_movie_rating

movie_csv_url = 'https://school.cefalolab.com/assignment/python/movies.csv'
rating_csv_url = 'https://school.cefalolab.com/assignment/python/ratings.csv'


def download_csv(url, filename):
    req = requests.get(url, verify=False)
    url_content = req.content

    csv_file = open(filename, 'wb')
    csv_file.write(url_content)
    csv_file.close()


def csv_to_list(filename):
    csv_file = open(filename)
    return list(csv.DictReader(csv_file))


# Downloading files
download_csv(movie_csv_url, 'movies.csv')
download_csv(rating_csv_url, 'ratings.csv')

# Initializing dictionaries
movies = csv_to_list('movies.csv')
ratings = csv_to_list('ratings.csv')

print('Mapping ratings...')
print('Stay put. This could take some minutes 🤓')

for rating in ratings:
    for key, value in enumerate(movies):
        if value['movieId'] == rating['movieId']:
            if 'number_of_ratings' not in value:
                value['number_of_ratings'] = 0
                value['ratings'] = []
                value['release'] = ''

            year = re.findall('\(\d{4}\)', value['title'])

            if len(year):
                value['release'] = year[0][1:-1]
                value['title'] = value['title'].replace(year[0], '').strip()
            else:
                value['title'] = value['title'].strip()

            value['number_of_ratings'] += 1
            value['ratings'].append(float(rating['rating']))

            break

print('Updating database...')

for movie in movies:
    if 'number_of_ratings' in movie:
        update_movie_rating(movie)
