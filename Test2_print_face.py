"""
Created by Antonino Abeshi
CS455 Artificial Intelligence Class
Due 04/25/2020

"""

import cv2
"""
Here we have the the germanlady cascade and the hatter cascade classifier.

"""

german_lady_cascade = cv2.CascadeClassifier('/home/gunesfjor/PycharmProjects/SchoolProjectAI/germanladyData/cascade.xml')
hatter_cascade = cv2.CascadeClassifier('/home/gunesfjor/PycharmProjects/SchoolProjectAI/hatterData/cascade.xml')
#earbud_cascade = cv2.CascadeClassifier('/home/gunesfjor/PycharmProjects/SchoolProjectAI/data3/cascade.xml')
cap = cv2.VideoCapture(0)

""" 
Recording the video.
Below we observe the w and h of the frame. I intend to record the video each time, thus 
I have created the mp4v video format fourcc, and the video_recording variable which saves the video with the name
Combined.mp4

"""


w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_recording = cv2.VideoWriter('Take1.mp4',fourcc, 20, (int(w), int(h)))

while (True):
    ret, img = cap.read()
    if ret == True:
        frame = cv2.flip(img, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray)

    # add this
    # image, reject levels level weights.

    german_lady = german_lady_cascade.detectMultiScale(
        gray,  # grayscale image
        scaleFactor=3,  # scaleFactor (worked on this until it got it correctly)
        minNeighbors=11,
        minSize=(20, 20),  # size of the image this was adjusted based on the scale of the image
    )
    # add this
    for (x,y,w,h) in german_lady:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  #detections
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'German Lady', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
# ------------------------------HATTER------------------------------------------------------------
    hatter = hatter_cascade.detectMultiScale(
        gray,  # grayscale image
        scaleFactor=5,  # scaleFactor (worked on this until it got it correctly)
        minNeighbors=11,
        minSize=(20, 20),  # size of the image this was adjusted based on the scale of the image
    )
    # add this
    for (x, y, w, h) in hatter:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # detections
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Hatter', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)


    # writting the flipped frame
    video_recording.write(img)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
