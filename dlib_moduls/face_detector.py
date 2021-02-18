import dlib
from skimage import io
from scipy.spatial import distance

predictor = dlib.shape_predictor('dlib_moduls/shape_predictor_5_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()
face_recognition = dlib.face_recognition_model_v1('dlib_moduls/dlib_face_recognition_resnet_model_v1.dat')


def get_info_points_face(image) -> dict:
    dets = detector(image, 1)
    faces = {}

    for k, d in enumerate(dets):
        points_list = []
        shape = predictor(image, d)
        descriptor = str(face_recognition.compute_face_descriptor(image, shape)).split('\n')
        descriptor = list(map(float, descriptor))

        for i in range(shape.num_parts):
            p = shape.part(i)
            points_list.append((p.x, p.y))

            faces.update({f'face_{k}': {
                'rectangle_points': {
                    'left': d.left(),
                    'top': d.top(),
                    'right': d.right(),
                    'bottom': d.bottom()
                },
                'points': points_list,
                'descriptor': descriptor}
            })

    return faces


def get_rectangle(face):
    if type(face) is dict:
        rectangle = dlib.rectangle(face['rectangle_points']['left'],
                                   face['rectangle_points']['top'],
                                   face['rectangle_points']['right'],
                                   face['rectangle_points']['bottom'],
                                   )
    else:
        rectangle = dlib.rectangle(face.rec_left,
                                   face.rec_top,
                                   face.rec_right,
                                   face.rec_bottom
                                   )
    return rectangle


def get_image(image_path: str):
    image = io.imread(image_path)
    return image


def get_descriptor(desc):
    descriptor = desc.split(',')
    descriptor = list(map(float, descriptor))
    return descriptor


def get_shape(image, rectangle):
    shape = predictor(image, rectangle)
    return shape


def get_distance(desc1, desc2):
    euclidean_distance = distance.euclidean(desc1, desc2)
    return euclidean_distance
