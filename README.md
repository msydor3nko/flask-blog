# flask-blog
The simple Blog on Python, Flask.
Has a basic blog features implementation such as user signup, user login, post creation, post like/unlike, analytics of likes summarized per day, saving last user login and user request logger.

# What do you need

**You need:** Git, Python3, pip.


# Follow the instructions to start the project

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


### Make database migration (by default used SQLite)

* Initialize database (reload venv if you get error)

`flask db init`

* Commit migration

`flask db migrate -m " creating tables from models"`

* Upgrade database tables

`flask db upgrade`

To rollback database tables use 'flask db downgrade'


### Fill data into DB

* To fill data into database use the next command:

`python fill_db.py`


### Run the App

* To run the app use the next command:

`flask run`