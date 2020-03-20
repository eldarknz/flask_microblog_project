from app import app_inst, db
from app.models import User, Post

@app_inst.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
