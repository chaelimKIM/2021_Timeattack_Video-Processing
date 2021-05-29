import cv2
import os
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from FaceRecognition import FaceRecognition as Fr


class FaceClustering:

    # 폴더 내의 이미지들 얼굴 인식
    @staticmethod
    def clustering(img_path):

#         descs = { }

        files = os.listdir(img_path)
#         #print("files = ", files)
#         path = {}
#         for i in files:
#             path.setdefault(i[:-4], str(img_path) + str(i))
#         #print("path = ", path)
#         FR = Fr(path, descs)
#         #FR.save_npy('FC')
#         # print("descs = ", descs)

        #얼굴 데이터
        faces = []
        #각각의 img에 몇명의 사람이 존재하는가
        faces_count = []

        for i in files:
            img_rgb = Fr.bgr2rgb(cv2.imread(str(img_path) + str(i)))
            _, shapes, _ = Fr.find_faces(img_rgb)
            n, descriptors = Fr.encode_faces(img_rgb, shapes)
            faces += descriptors
            faces_count.append(n)
        faces = np.array(faces)

        # clustering
        clt = DBSCAN(eps=0.5, metric="euclidean")
        # clt.fit(faces)

        kmeans = KMeans(n_clusters=4, random_state=0).fit(faces)
        kmeans.labels_

        print("kmeans labels")
        print(kmeans.labels_)
        # # label_ids = 얼굴 id
        # label_ids = np.unique(clt.labels_)
        # print("clt labels")
        # print(clt.labels_)
        # # num_unique_faces = label의 갯수
        # num_unique_faces = len(np.where(label_ids > -1)[0])
        #
        # print("num_unique_faces = ", num_unique_faces)
