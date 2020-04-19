import requests
import csv

movie_csv_url = 'https://school.cefalolab.com/assignment/python/movies.csv'
rating_csv_url = 'https://school.cefalolab.com/assignment/python/movies.csv'


req = requests.get(movie_csv_url, verify=False)
url_content = req.content

csv_file = open('movies.csv', 'wb')
csv_file.write(url_content)
csv_file.close()


with open('movies.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
    # for row in csv_reader:
    #     print(row)

    csv_reader_dict = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader_dict:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        line_count += 1
        print(row['title'])
