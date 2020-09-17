from datetime import datetime, timedelta
import random
from app import db
from app.models import User, Post, PostLike


# clear tables
User.query.delete()
Post.query.delete()
PostLike.query.delete()
db.session.commit()


# timestamps
now = datetime.utcnow()
one_day_ago = now - timedelta(days=1)
two_days_ago = now - timedelta(days=2)


# create useres
# author
kate = User(username='Kate', email='kate@example.com')
kate.set_password(password='1')
db.session.add(kate)
# liker
mike = User(username='Mike', email='mike@example.com')
mike.set_password(password='2')
db.session.add(mike)
# save users
db.session.commit()


# posts
kate_posts = [
    {
    "title" : "Post 1",
    "body" : 'Content of Post 1',
    "publication_day" : two_days_ago,
    "author" : kate
    },
    {
    "title" : "Post 2",
    "body" : 'Content of Post 2',
    "publication_day" : two_days_ago,
    "author" : kate
    },
    {
    "title" : "Post 3",
    "body" : 'Content of Post 3',
    "publication_day" : two_days_ago,
    "author" : kate
    },
    {
    "title" : "Post 4",
    "body" : 'Content of Post 4',
    "publication_day" : one_day_ago,
    "author" : kate
    },
    {
    "title" : "Post 5",
    "body" : 'Content of Post 5',
    "publication_day" : one_day_ago,
    "author" : kate
    },
    {
    "title" : "Post 6",
    "body" : 'Content of Post 6',
    "publication_day" : one_day_ago,
    "author" : kate
    },
    {
    "title" : "Post 7",
    "body" : 'Content of Post 7',
    "publication_day" : one_day_ago,
    "author" : kate
    },
    {
    "title" : "Post 8",
    "body" : 'Content of Post 8',
    "publication_day" : now,
    "author" : kate
    },
    {
    "title" : "Post 9",
    "body" : 'Content of Post 9',
    "publication_day" : now,
    "author" : kate
    },
    {
    "title" : "Post 10",
    "body" : 'Content of Post 10',
    "publication_day" : now,
    "author" : kate
    },
]


# putting posts and likes into db
for post in kate_posts:
    # new post
    new_post = Post(title=post["title"], body=post["body"], publication_day=post["publication_day"], author=post["author"])
    db.session.add(new_post)
    db.session.commit()
    # new like
    is_like = random.choices([True, False], weights=(80, 20))
    new_post_like = PostLike(like=is_like[0], liked_post=new_post, liked_by=mike, date=post["publication_day"])
    db.session.add(new_post_like)
    db.session.commit()