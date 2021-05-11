import cv2
import os
import numpy as np
from sklearn.cluster import DBSCAN
from FaceRecognition import FaceRecognition as Fr

class FaceClustering:

    def read_all_images(img_path):
        # 이미지 경로
        # 이미지 읽어오기
        descs = {
            'neo': None,
            'trinity': None,
            'morpheus': None,
            'smith': None
        }

        files = os.listdir(img_path)
        for i in files:
            path = str(img_path) + str(i)
            print(path)
            FR = Fr(path, descs)
            FR.save_npy() ###여기<<<
            print(descs)


    #수정중
    def cluster(self):
        encodings = [face.encoding for face in self.faces]

        # clustering
        clt = DBSCAN(metric="euclidean")
        clt.fit(encodings)

        # label_ids = 얼굴 id
        label_ids = np.unique(clt.labels_)
        # num_unique_faces = label의 갯수
        num_unique_faces = len(np.where(label_ids > -1)[0])

        # 얼굴 id
        for label_id in label_ids:
            # directory 만들기 / 해당 얼굴 그림 저장됨
            dir_name = "ID%d" % label_id
            os.mkdir(dir_name)

            # label에 해당하는 index를 모두 얻어옴
            indexes = np.where(clt.labels_ == label_id)[0]

            # label에 해당하는 모든 얼굴을 ID# 디렉토리에 저장
            for i in indexes:
                frame_id = self.faces[i].frame_id
                box = self.faces[i].box
                pathname = os.path.join(self.capture_dir,
                                        self.capture_filename(frame_id))
                image = cv2.imread(pathname)
                face_image = self.getFaceImage(image, box)
                filename = dir_name + "-" + self.capture_filename(frame_id)
                pathname = os.path.join(dir_name, filename)
                cv2.imwrite(pathname, face_image)