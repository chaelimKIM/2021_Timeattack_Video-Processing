import cv2
import os
import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from FaceRecognition import FaceRecognition as Fr


class FaceClustering:
    def __init__(self, img_path):
        self.img_path = img_path
        self.files = os.listdir(img_path)
        self.path = []
        for i in self.files:
            self.path.append(str(img_path) + str(i))
        self.faces = []
        self.faces_count = []    # 각각의 img에 몇명의 사람이 존재하는가
        self.kmeans = None

    # 폴더 내의 이미지들 얼굴 인식
    def clustering(self):
        for i in self.files:
            img_rgb = Fr.bgr2rgb(cv2.imread(str(self.img_path) + str(i)))
            _, shapes, _ = Fr.find_faces(img_rgb)
            n, descriptors = Fr.encode_faces(img_rgb, shapes)
            self.faces += descriptors
            self.faces_count.append(n)
        faces = np.array(self.faces)

        # clustering
        # clt = DBSCAN(eps=0.5, metric="euclidean")
        # clt.fit(faces)

        self.kmeans = KMeans(n_clusters=4, random_state=0).fit(faces)

        print("kmeans labels =", self.kmeans.labels_)

    def rep_img(self):
        rep_img_paths = []  # 대표이미지 경로 저장
        label_indexs = []
        cluster_count = 4  # 클러스터링 할 인물 수
        c = 0
        while c < cluster_count:
            rep_img_paths.append('')
            label_indexs.append(0)
            c += 1

        k = 0
        c = 0
        for i in self.faces_count:
            for j in range(c, c + i - 1):
                # print(path[k])
                id = self.kmeans.labels_[j]
                if rep_img_paths[id] == '':
                    rep_img_paths[id] = str(self.path[k])
                    label_indexs[id] = j
                else:
                    if np.linalg.norm(self.kmeans.cluster_centers_[id] - self.faces[j]) < \
                            np.linalg.norm(self.kmeans.cluster_centers_[id] - self.faces[label_indexs[id]]):
                        rep_img_paths[id] = str(self.path[k])
                        label_indexs[id] = j
                c = c + i
            k += 1

        return rep_img_paths, label_indexs

    def save_result(self, label_index, up_id):
        target = self.kmeans.labels_[label_index]
        i = 0
        for lab in self.kmeans.labels_:
            target_path = self.path[i]
            if lab == target:
                img = cv2.imread(target_path)
                cv2.imwrite("C:/Users/MunsuYu/TimeAttack/TimeAttackFile/result/" + target_path[11+len(str(up_id)):],
                            img)
            i += 1
