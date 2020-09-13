# flask-blog
The simple Blog on Python, Flask

## What do you need

**You need:** Git, Python3, pip.


## Following by steps

### Setup environment

* Clone the App repository using Git

`git clone https://github.com/msydor3nko/flask-blog.git`

* Enter to the 'flask-blog' directory

`cd flask-blog`

* Create and activate virtual environment

`python3 -m venv venv`

`source venv/bin/activate`

* Install all required libraries from 'requirements.txt'

`pip install -r requirements.txt`


### Make database migration (by default using SQLite)

* Init database

`flask db init`

* Commit migration

`flask db migrate -m " creating tables from models"`

* Upgrade database tables

`flask db upgrade`

To rollback database tables use 'flask db downgrade'


### Run the App

* Run 'blog.py' file using command

`python blog.py`




