import os

db_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(db_dir, 'db_image/face_definition.db')
UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
SQLALCHEMY_TRACK_MODIFICATIONS = False
