import cv2
from FaceRecognition import FaceRecognition as Fr
from VideoSlicing import VideoSlicing as Vs
from FaceClustering import FaceClustering as Fc
from DB import DB

# main
DB = DB()
up_id = DB.select_upid_by_processing()

up_vid_path = DB.select_upvidpath(up_id)
VS = Vs(up_vid_path, up_id)
VS.slicing()

FC = Fc("./slicing/" + str(up_id) + "/")
FC.clustering()

FR = Fr()
up_img_path = DB.select_upimgpath(up_id)
up_img = cv2.imread(up_img_path)
rep_img_paths, label_indexs = FC.rep_img()
i = 0
for rep_img_path in rep_img_paths:
    label_index = label_indexs[i]
    rep_img = cv2.imread(rep_img_path)
    if FR.compare_faces(rep_img, up_img):
        FC.save_result(label_index, up_id)
        break
    i += 1

# # test
# FC = Fc("./slicing/1/")
# FC.clustering()
# rep_img_paths, label_indexs = FC.rep_img()
# i = 0
# for rep_img_path in rep_img_paths:
#     label_index = label_indexs[i]
#     i += 1
#     print("rep_img_path =", rep_img_path)
#     print("ㄴlabel_index =", label_index)
#     # rep_img = cv2.imread(rep_img_path)
#     # if FR.compare_faces(rep_img, up_img):
#     #     break
