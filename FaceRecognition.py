import dlib
import cv2
import numpy as np

# dlib의 얼굴 검출기 이용
detector = dlib.get_frontal_face_detector()
# 인식된 얼굴에서 랜드마크 찾기
sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")


class FaceRecognition:

    @staticmethod
    def find_faces(img):  # 얼굴 인식
        dets = detector(img, 1)  # 얼굴이 인식된 영역을 dets에 저장

        # 탐지된 얼굴이 없으면 0 반환
        if len(dets) == 0:
            return np.empty(0), np.empty(0), np.empty(0)

        # 탐지됬을 때만
        rects, shapes = [], []
        shapes_np = np.zeros((len(dets), 68, 2), dtype=int)
        for k, d in enumerate(dets):
            # 인식된 얼굴 영역의 좌표를 rects에 저장
            rect = ((d.left(), d.top()), (d.right(), d.bottom()))
            rects.append(rect)

            # 인식된 얼굴 영역에서 점 68개를 추출해 그 좌표를 shapes에 저장
            shape = sp(img, d)
            shapes.append(shape)

            # shape를 넘파이배열 형식으로 변환하여 shapes_np에 저장
            for i in range(0, 68):
                shapes_np[k][i] = (shape.part(i).x, shape.part(i).y)

        return rects, shapes, shapes_np

    @staticmethod
    def encode_faces(img, shapes):  # 68개의 점을 128개의 벡터로 변환
        face_descriptors = []
        count = 0
        for shape in shapes:
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            face_descriptors.append(face_descriptor)
            count = count + 1

        return count, face_descriptors

    @staticmethod
    def bgr2rgb(img_bgr):  # bgr 형식 이미지를 rgb 형식 이미지로 바꾸는 함수
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        return img_rgb

    def compare_faces(self, img1, img2):  # rgb형식의 이미지 2개를 비교
        tf = False
        img1 = self.bgr2rgb(img1)
        img2 = self.bgr2rgb(img2)
        _, shapes1, _ = self.find_faces(img1)
        _, descriptors1 = self.encode_faces(img1, shapes1)
        _, shapes2, _ = self.find_faces(img2)
        _, descriptors2 = self.encode_faces(img2, shapes2)

        dist = np.linalg.norm(np.array(descriptors1) - np.array(descriptors2), axis=1)
        if np.any(dist) < 0.6:  # 같은 얼굴로 판별하는 기준
            tf = True

        return tf
