from sqlalchemy import Column, Integer, String

from .datasbase import db


class FaceInfo(db.Model):
    __tablename__ = 'face_info'
    id = Column(Integer, primary_key=True)
    rec_left = Column(Integer, nullable=False)
    rec_top = Column(Integer, nullable=False)
    rec_right = Column(Integer, nullable=False)
    rec_bottom = Column(Integer, nullable=False)
    face_points = Column(String, nullable=False)
    descriptor = Column(String, nullable=False)
    image_path = Column(String, nullable=False)

