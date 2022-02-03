import cv2
import time

if __name__ == '__main__':
    cap = cv2.VideoCapture(-1) # 任意のカメラ番号に変更する
    image = None
    try:
        print("capture start")
        while True:
            ret, frame = cap.read()
            time.sleep(0.01)
            image = frame
    except KeyboardInterrupt:
        cv2.imwrite('frame.png', image)
        pass
    cap.release()
    print("done")