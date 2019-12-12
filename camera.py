from time import time
import cv2

class Camera(object):

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def get_frame(self):
        ret, frame = self.cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        file1 = cv2.imwrite('1.jpg',rgb)
        #time.sleep(0.01)
        imgs = open('1.jpg', 'rb').read()
        return imgs
    def __del__(self):
        self.cap.release()    