import dlib
import cv2
import numpy as np

# dlib의 얼굴 검출기 이용
detector = dlib.get_frontal_face_detector()
# 인식된 얼굴에서 랜드마크 찾기
sp = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('models/dlib_face_recognition_resnet_model_v1.dat')


class FaceRecognition:

    def __init__(self, img_paths, descs):
        self.img_paths = img_paths
        self.descs = descs

    def find_faces(self, img):
        dets = detector(img, 1)

        if len(dets) == 0:
            return np.empty(0), np.empty(0), np.empty(0)

        rects, shapes = [], []
        shapes_np = np.zeros((len(dets), 68, 2), dtype=int)
        for k, d in enumerate(dets):
            rect = ((d.left(), d.top()), (d.right(), d.bottom()))
            rects.append(rect)

            shape = sp(img, d)
            shapes.append(shape)

            # convert dlib shape to numpy array
            for i in range(0, 68):
                shapes_np[k][i] = (shape.part(i).x, shape.part(i).y)

        return rects, shapes, shapes_np

    def encode_faces(self, img, shapes):
        face_descriptors = []
        for shape in shapes:
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            face_descriptors.append(np.array(face_descriptor))

        return np.array(face_descriptors)

    def bgr2rgb(self, img_bgr):
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        return img_rgb

    def save_npy(self):
        for name, img_path in self.img_paths.items():
            img_rgb = self.bgr2rgb(cv2.imread(img_path))

            _, img_shapes, _ = self.find_faces(img_rgb)
            self.descs[name] = self.encode_faces(img_rgb, img_shapes)[0]

        np.save('img/descs.npy', self.descs)
