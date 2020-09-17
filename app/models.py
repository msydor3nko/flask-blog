from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login


# UserMixin implemented to User class 4 Flask-Login properties:
# 'is_authenticated', 'is_active', 'is_anonymous', 'get_id'
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    # last login
    last_visit = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    
    # One User <- many posts
    posts = db.relationship('Post', backref='author')
    # One User <- many likes
    likes = db.relationship('PostLike', backref='liked_by')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {} : {}>'.format(self.username, self.id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publication_day = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    title = db.Column(db.String(80))
    body = db.Column(db.String(200))
    
    # Many posts -> one user
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # One post <- many likes
    likes = db.relationship('PostLike', backref='liked_post')
    
    def __repr__(self):
        return '<PostID-Title {} : {}>'.format(self.id, self.title)


class PostLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    
    like = db.Column(db.Boolean, nullable=False)    # like or dislike
    
    # Many likes -> one post
    liked_post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    
    # Many likes -> one user
    liked_by_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

# Flask-Login keeps track of the logged in user by storing its unique identifier in Flask’s user session
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
