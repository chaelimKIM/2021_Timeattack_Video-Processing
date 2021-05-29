import cv2
from FaceRecognition import FaceRecognition as Fr
from VideoSlicing import VideoSlicing as Vs
from FaceClustering import FaceClustering as Fc
from DB import DB

DB = DB()
up_id = DB.select_upid_by_processing()

up_vid_path = DB.select_upvidpath(up_id)
VS = Vs(up_vid_path, up_id)

FR = Fr()
up_img_path = DB.select_upimgpath(up_id)
up_img = cv2.imread(up_img_path)
rep_img_paths = Fc.clustering("./slicing/" + str(up_id) + "/")
for rep_img_path in rep_img_paths:
    rep_img = cv2.imread(rep_img_path)
    if FR.compare_faces(rep_img, up_img):
        # result에 저장
        break
