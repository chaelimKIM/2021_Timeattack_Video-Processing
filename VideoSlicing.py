import cv2
import datetime
import CreateDirectory


class VideoSlicing:

    def __init__(self, up_vid_path, up_id):
        self.video = cv2.VideoCapture(up_vid_path)  # 동영상 입력 경로
        self.up_id = up_id

    def slicing(self):
        CreateDirectory.create('slicing/' + str(self.up_id))
        count = 0
        fps = int(self.video.get(cv2.CAP_PROP_FPS))

        while self.video.isOpened():
            ret, frame = self.video.read()

            # 프레임 존재하지 않을 경우 break
            if not ret:
                break

            if int(self.video.get(1)) % fps == 0:
                # 현재 시간
                # now = datetime.datetime.now().strftime("%d_%H-%M-%S__")

                # 캡쳐한 이미지 저장 경로
                cv2.imwrite("slicing/" + str(self.up_id) + "/" + str(count) + ".png", frame)
                count += 1

        self.video.release()
