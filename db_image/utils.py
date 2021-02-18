from .model import FaceInfo
from .datasbase import db

from dlib_moduls.face_detector import get_descriptor, get_distance


def insert_data_in_db(face, faces, img_path):
    descriptor1 = face['descriptor']
    face_data = FaceInfo(
        rec_left=face['rectangle_points']['left'],
        rec_top=face['rectangle_points']['top'],
        rec_right=face['rectangle_points']['right'],
        rec_bottom=face['rectangle_points']['bottom'],
        face_points=str(face['points']).strip('[]'),
        descriptor=str(face['descriptor']).strip('[]'),
        image_path=img_path
    )
    count = face_check(descriptor1, faces)
    if not count:
        db.session.add(face_data)
    db.session.commit()
    db.session.close()


def face_check(desc, faces) -> int:
    """Проверка на наличия лица в бд"""
    count = 0
    if faces:
        for face in faces:
            descriptor2 = get_descriptor(face.descriptor)
            distance = get_distance(desc, descriptor2)
            if distance == 0.0:
                count += 1
        db.session.close()
    else:
        return count
    return count
