"""
Created by Antonino Abeshi
CS455 Artificial Intelligence Class
Due 04/25/2020

"""

import cv2

"""
Here we have the three cascades all together. The xml files have been trained and are used in the 
CascadeClassifier. 
"""

german_lady_cascade = cv2.CascadeClassifier('germanladyData/cascade.xml')
hatter_cascade = cv2.CascadeClassifier('hatterData/cascade.xml')
earbud_cascade = cv2.CascadeClassifier('earpodsData/cascade.xml')

# Capturing the video
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
video_recording = cv2.VideoWriter('Combined.mp4',fourcc, 20, (int(w), int(h)))


while (True):
    """
    While true we set the ret and the img variables to read the video capture.
    We flip the frames of the image and give it the gray color.
    """
    ret, img = cap.read()
    if ret == True:
        frame = cv2.flip(img, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray)

    # add this
    # image, reject levels level weights.

    """
    Here are my adjustements to reading the image better when recorded. We can select the scaleFactor, which is a 
    parameter that specifies how much the image size is reduced at each image scale; we have minNeighboors which 
    specifies how many neighbors each candidate rectangle should have to retain it; minSize which means the minimum
    possible object size. Objects smaller are ignored. 
    """
    german_lady = german_lady_cascade.detectMultiScale(
        gray,  # grayscale image
        scaleFactor=3,  # scaleFactor (worked on this until it got it correctly)
        minNeighbors=11,
        minSize=(50, 50),  # size of the image this was adjusted based on the scale of the image
    )
    # add this
    """
    Below we create the image selection, as a rectangle, but there are options to do it as a circle as well, 
    and we select the color which are the 255,255,0, which mean GRB colors(GREEN,RED,BLUE). I also include a text
    above the image to make it more recognisable. This is done fo all the images that we want to recognise,
    but different colors are included and different titles are inputed.
    """
    for (x,y,w,h) in german_lady:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  # these mean detections in the form of a rectangle
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

# -----------------------------------EARBUDS--------------------------------------------------------

    earbuds = earbud_cascade.detectMultiScale(
        gray,  # grayscale image
        scaleFactor=3,  # scaleFactor (worked on this until it got it correctly)
        minNeighbors=11,
        minSize=(50, 50),  # size of the image this was adjusted based on the scale of the image
    )
    # add this
    for (x, y, w, h) in earbuds:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)  # detections
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'earbuds', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

    # writting the flipped frame
    video_recording.write(img)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
