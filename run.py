from app import create_app, db
from app.models import User,ExtendedUser

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, ExtendedUser=ExtendedUser)


if __name__ == '__main__':
    app.run(debug=True)
