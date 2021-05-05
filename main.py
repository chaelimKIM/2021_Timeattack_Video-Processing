import cv2
import datetime

# 동영상 입력 경로
video = cv2.VideoCapture("sample.mp4")

count = 0

while video.isOpened():
    ret, frame = video.read()

    #프레임 존재하지 않을 경우 break
    if not ret:
        break

    # 현재 시간
    now = datetime.datetime.now().strftime("%d_%H-%M-%S__")

    # 캡쳐한 이미지 저장 경로
    cv2.imwrite("C:/Users/Y/Desktop/coding/sample/" + str(now) + str(count) + ".png", frame)
    count += 1

video.release()