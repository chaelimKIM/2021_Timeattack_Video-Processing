import cv2
from FaceRecognition import FaceRecognition as Fr
from VideoSlicing import VideoSlicing as Vs
from FaceClustering import FaceClustering as Fc
from DB import DB

# main
# DB = DB()
# up_id = DB.select_upid_by_processing()

# up_vid_path = DB.select_upvidpath(up_id)
# VS = Vs(up_vid_path, up_id)
#
# Fc.clustering("./slicing/" + str(up_id) + "/")
#
# FR = Fr()
# up_img_path = DB.select_upimgpath(up_id)
# up_img = cv2.imread(up_img_path)
# clt_img_paths = []
# for clt_img_path in clt_img_paths:
#     clt_img = cv2.imread(clt_img_path)
#     if FR.compare_faces(clt_img, up_img):
#         result쪽으로 클러스터 이미지들 저장
#         break

# fC 클래스 테스트
# img_path_dir = './slicing/'
# Fc.clustering(img_path_dir)
