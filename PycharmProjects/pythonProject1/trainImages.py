# In this module we are trying to train the images that are collected by video recording and
# after that we are traing that images
# Then we are placing that trained data set in the fire base storage bucket

import cv2 as cv
# import kivy
from matplotlib import pyplot as py
import numpy as np
from firebaseconnection import OpenFireBaseConnection


class FaceTrainer:
    def __init__(self):
        self.face_cascade = cv.CascadeClassifier('./HaarCascadesFiles/haarcascade_frontalface_default.xml')
        self.face_recognizer = None

    def detect_face(self, image):
        img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(img, 1.2, minNeighbors=5)
        return faces, img

    def showplotDiagram(self):
        if len(self.setOfImages) > 0:
            for i in range(len(self.setOfImages)):
                py.subplot(2, 10, i + 1)
                py.imshow(self.setOfImages[i], 'gray')
            py.show()

    def collect_images(self):
        try:
            capture = cv.VideoCapture(0)
            setOfImages = []
            setOfIds = []
            count = 0
            while capture.isOpened():
                isTrue, frame = capture.read()
                faces, gray_frame = self.detect_face(frame)
                if len(faces) == 1:
                    x, y, w, h = faces[0]
                    cv.rectangle(frame, (x, y), (x + h, y + w), (255, 0, 0), 2)
                    setOfImages.append(gray_frame[y:y + w, x:x + h])
                    setOfIds.append(1)
                    count += 1
                cv.imshow('myface', frame)
                if cv.waitKey(10) & 0xFF == ord('d') or count > 10:
                    break
            capture.release()
            cv.destroyAllWindows()
            self.setOfImages = setOfImages
            self.setOfIds = setOfIds
        except Exception as e:
            return e
        finally:
            # it will shows the polt diagram of the traingin set use it just for debuging perposes
            # self.showplotDiagram();
            return self

    def train_the_set(self, save_directory='dummy'):

        face_recognizer = cv.face.LBPHFaceRecognizer_create()
        face_recognizer.train(self.setOfImages, np.array(self.setOfIds))
        try:
            face_recognizer.save('mytrainingset.txt')
            OpenFireBaseConnection().storage.child(save_directory).put('./mytrainingset.txt')
        except Exception as e:
            pass
        self.face_recognizer = face_recognizer
        return self

    def recognize_face(self):
        try:
            capture = cv.VideoCapture(0)
            if (self.face_recognizer == None):
                self.face_recognizer = cv.face.LBPHFaceRecognizer_create()
                self.face_recognizer.read('./mytrainingset.txt')
            while capture.isOpened():
                isTrue, frame = capture.read()
                faces, gray = self.detect_face(frame)
                for (x, y, w, h) in faces:
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                if (len(faces) == 1):
                    x, y, w, h = faces[0]
                    roi_gray = gray[y:y + w, x:x + h]
                    label, confidence = self.face_recognizer.predict(roi_gray)
                    if confidence < 40:
                        capture.release()
                        cv.destroyAllWindows()
                        print('yes we got you')
                        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        return True
                cv.imshow("capturing face to take attendence", frame)
                if cv.waitKey(10) & 0xFF == ord('d'):
                    break
            capture.release()
            cv.destroyAllWindows()
        except Exception as e:
            return e


if __name__ == '__main__':
    FaceTrainer().collect_images().train_the_set().recognize_face()
