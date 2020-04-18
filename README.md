# movie-scrapper
Scrap movie data from various sources and serve the information using API 

This project uses `pipenv` as a package management tool. If you don't have `pipenv` installed, then install it by

``` bash
pip install pipenv
```

### Quick Start Using Pipenv

``` bash
# Activate virtual env
$ pipenv shell

# Install dependencies
$ pipenv install

# Run Server (http://localhst:5000)
python app.py
```

### To fresh create DB, remove `db.sqlite` file
``` bash
$ python
>> from app import db
>> db.create_all()
>> exit()
```

### API Endpoints

* GET     /movie
* GET     /movie/:id
* POST    /movie
* PUT     /movie/:id
* DELETE  /movie/:id