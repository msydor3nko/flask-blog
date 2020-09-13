from app import app, db
from app.models import User, Post


# shell context setup for 'flask shell' command
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.run(debug=True)
