import os

from flask import Flask, request
from flask_restful import Api, Resource
from flask_migrate import Migrate

import config
from db_image import db, FaceInfo
from dlib_moduls import face_detector as fd
from db_image.utils import insert_data_in_db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    UPLOAD_FOLDER=config.UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS=config.ALLOWED_EXTENSIONS,
    SQLALCHEMY_TRACK_MODIFICATIONS=config.SQLALCHEMY_TRACK_MODIFICATIONS,

)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS


class ImageAnalysis(Resource):
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            image_path = config.UPLOAD_FOLDER + file.filename
            file.save(image_path)
            image = fd.get_image(image_path)
            faces = fd.get_info_points_face(image)
            faces_in_db = FaceInfo.query.all()
            for face in faces.values():
                insert_data_in_db(face, faces_in_db, image_path)
                del face['descriptor']
            return faces

        return {'error': f'Invalid file format! Valid format: '
                         f'{config.ALLOWED_EXTENSIONS}'}


class FaceVerification(Resource):
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            path_dir = create_dir('images/for_removing/')
            path_new_image = path_dir + file.filename
            famous_faces = FaceInfo.query.all()
            file.save(path_new_image)
            new_image = fd.get_image(path_new_image)
            faces_in_image = fd.get_info_points_face(new_image)
            count_face_in_image = len(faces_in_image)
            count_verification_faces = 0
            for face_in_image in faces_in_image.values():
                descriptor1 = face_in_image['descriptor']

                for famous_face in famous_faces:
                    descriptor2 = fd.get_descriptor(famous_face.descriptor)
                    distance = fd.get_distance(descriptor1, descriptor2)
                    if distance < 0.5:
                        count_verification_faces += 1

            os.remove(path_new_image)
            return {'face_in_image': count_face_in_image,
                    'verification_face': count_verification_faces}
        return {'error': f'Invalid file format! Valid format: '
                         f'{config.ALLOWED_EXTENSIONS}'}


api.add_resource(ImageAnalysis, '/image_analysis')
api.add_resource(FaceVerification, '/face_verification')


def create_dir(path: str) -> str:
    if not os.path.exists('images/for_removing/'):
        os.mkdir('images/for_removing/')
    return path
