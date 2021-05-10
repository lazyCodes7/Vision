import cv2;

from SpeechHandling import *


def checkFaces():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

    video = cv2.VideoCapture(0);
    check, frame = video.read();
    faces = face_cascade.detectMultiScale(frame,
                                          scaleFactor=1.1, minNeighbors=5);
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3);

    if(len(faces)>0):

    	speak("Number of faces detect are {}".format(len(faces)))


    video.release();
    cv2.destroyAllWindows();

