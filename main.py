import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
from FaceRecognition import FaceRecognition as Fr
from VideoSlicing import VideoSlicing as Vs
from FaceClustering import FaceClustering as Fc

# 영상 slicing
#VS = Vs()
#VS.slicing()

# main에서 테스트하기 위해 특정 경로의 특정 파일 지정
img_paths = {
   'neo': 'img/neo.jpg',
   'trinity': 'img/trinity.jpg',
   'morpheus': 'img/morpheus.jpg',
   'smith': 'img/smith.jpg'
}

descs = {
    'neo': None,
    'trinity': None,
    'morpheus': None,
    'smith': None
}

# fC 클래스에서 FR클래스 테스트
img_path_dir = './slicing/'
Fc.clustering(img_path_dir)

#
# # main에서 FR 클래스 테스트
FR = Fr(img_paths, descs)
# FR.save_npy('m5')
# img_rgb = FR.bgr2rgb(cv2.imread('img/matrix5.jpg'))
# rects, shapes, _ = FR.find_faces(img_rgb)
# descriptors = FR.encode_faces(img_rgb, shapes)

# compare_faces 테스트
img1 = cv2.imread('img/1.jpg')
img2 = cv2.imread('img/2.jpg')
tf = FR.compare_faces(img1, img2)
print(tf)

# # Visualize Output
# fig, ax = plt.subplots(1, figsize=(10, 10))
# ax.imshow(img_rgb)
#
# for i, desc in enumerate(descriptors):
#
#     found = False
#     for name, saved_desc in descs.items():
#         dist = np.linalg.norm([desc] - saved_desc, axis=1)    # 유클리디안 거리
#
#         if dist < 0.6:
#             found = True
#
#             text = ax.text(rects[i][0][0], rects[i][0][1], name, color='b', fontsize=40, fontweight='bold')
#             text.set_path_effects([path_effects.Stroke(linewidth=10, foreground='white'), path_effects.Normal()])
#             rect = patches.Rectangle(rects[i][0], rects[i][1][1] - rects[i][0][1],
#                                      rects[i][1][0] - rects[i][0][0],
#                                      linewidth=2, edgecolor='w', facecolor='none')
#             ax.add_patch(rect)
#
#             break
#
#     if not found:
#         ax.text(rects[i][0][0], rects[i][0][1], 'unknown',
#                 color='r', fontsize=20, fontweight='bold')
#         rect = patches.Rectangle(rects[i][0], rects[i][1][1] - rects[i][0][1],
#                                  rects[i][1][0] - rects[i][0][0],
#                                  linewidth=2, edgecolor='r', facecolor='none')
#         ax.add_patch(rect)
#
# plt.axis('off')
# plt.savefig('result/output.png')
# plt.show()
