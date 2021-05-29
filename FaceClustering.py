import cv2
import os
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from FaceRecognition import FaceRecognition as Fr


class FaceClustering:

    # 폴더 내의 이미지들 얼굴 인식
    @staticmethod
    def clustering(img_path):
        files = os.listdir(img_path)
        # print("files = ", files)
        path = []
        for i in files:
            path.append(str(img_path) + str(i))
        # print(path)

        # 얼굴 데이터
        faces = []
        # 각각의 img에 몇명의 사람이 존재하는가
        faces_count = []

        for i in files:
            img_rgb = Fr.bgr2rgb(cv2.imread(str(img_path) + str(i)))
            _, shapes, _ = Fr.find_faces(img_rgb)
            n, descriptors = Fr.encode_faces(img_rgb, shapes)
            faces += descriptors
            faces_count.append(n)
        faces = np.array(faces)

        # clustering
        # clt = DBSCAN(eps=0.5, metric="euclidean")
        # clt.fit(faces)

        kmeans = KMeans(n_clusters=4, random_state=0).fit(faces)
        kmeans.labels_

        print("kmeans labels")
        print(kmeans.labels_)

        rep_img_paths = []    # 대표이미지 경로 저장
        image_label = []
        cluster_count = 4    # 클러스터링 할 인물 수
        c = 0
        while c < cluster_count:
            rep_img_paths.append('')
            image_label.append(0)
            c += 1

        k = 0
        c = 0
        for i in faces_count:
            for j in range(c, c+i):
                # print(path[k])
                id = kmeans.labels_[j]
                if rep_img_paths[id] == '':
                    rep_img_paths[id] = str(path[k])
                    image_label[id] = j
                else:
                    if np.linalg.norm(kmeans.cluster_centers_[id] - faces[j]) < \
                       np.linalg.norm(kmeans.cluster_centers_[id] - faces[image_label[id]]):
                        rep_img_paths[id] = str(path[k])
                        image_label[id] = j
                c = c + i
            k += 1

        return rep_img_paths
        # print(image_label)
