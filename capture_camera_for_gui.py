import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture(-1) # 任意のカメラ番号に変更する
    while True:
        ret, frame = cap.read()
        cv2.imshow("camera", frame)

        k = cv2.waitKey(1) # キー入力を待つ
        if k == ord('q'):
            cv2.imwrite('frame.png', frame)
            break     #「q」キーが押されたら終了する

    # キャプチャをリリースして、ウィンドウをすべて閉じる
    cap.release()
    cv2.destroyAllWindows()