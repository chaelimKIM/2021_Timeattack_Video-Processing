import cv2
import datetime


class VideoSlicing:

    def __init__(self):
        self.video = cv2.VideoCapture("vid/sample.mp4")    # 동영상 입력 경로

    def slicing(self):
        count = 0
        while self.video.isOpened():
            ret, frame = self.video.read()

            # 프레임 존재하지 않을 경우 break
            if not ret:
                break

            # 현재 시간
            now = datetime.datetime.now().strftime("%d_%H-%M-%S__")

            # 캡쳐한 이미지 저장 경로
            cv2.imwrite("slicing/" + str(now) + str(count) + ".png", frame)
            count += 1

        self.video.release()