"""
Created by Antonino Abeshi
CS455 Artificial Intelligence Class
Due 04/25/2020

"""

import cv2

"""
Here we have my first cascades. I experimented with a few lke different soccer balls. It din't work very well.
Continuing I used the earbud. It worked well.
 
"""

#this is the cascade we just made. Call what you want
#football_cascade = cv2.CascadeClassifier('/home/gunesfjor/PycharmProjects/SchoolProjectAI/data/football-cascade-8stages.xml')
#football2_cascade = cv2.CascadeClassifier('/home/gunesfjor/PycharmProjects/SchoolProjectAI/data2/cascade.xml')
earbud_cascade = cv2.CascadeClassifier('/home/gunesfjor/PycharmProjects/SchoolProjectAI/earpodsData/cascade.xml')
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
video_recording = cv2.VideoWriter('TakeEarpods.mp4',fourcc, 20, (int(w), int(h)))

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray)

    # add this
    # image, reject levels level weights.
    #football = football_cascade.detectMultiScale(gray, 50, 50)
    #football2 = football2_cascade.detectMultiScale(gray, 20, 20)
    #earbuds = earbud_cascade.detectMultiScale(gray, 2, 11, 50)
    earbuds = earbud_cascade.detectMultiScale(
        gray, # grayscale image
        scaleFactor=3,  # scaleFactor (worked on this until it got it correctly)
        minNeighbors=11,
        minSize=(50, 50), # size of the image this was adjusted based on the scale of the image
    )
    # add this
    for (x,y,w,h) in earbuds:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  #detections
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'earbuds', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)

    # writting the flipped frame
    video_recording.write(img)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
