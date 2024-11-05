from flask_app_api import app, db

with app.app_context():
    db.create_all()