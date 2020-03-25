from flask import render_template
from app import app_inst, db

@app_inst.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app_inst.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app_inst.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403
