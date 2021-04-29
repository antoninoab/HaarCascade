#Welcome to my Haar Cascade Image and Video Object Classificication  

#The program runs only through terminal, it does not run through Pycharm (gives Sigil for some reason)
Before running the program:
- Imporant libraries to install:
	- Opencv 
	- Numpy
- Linux (my prefered workspace, the program works best and easiest)
	- Install opencv-python
	- Install numpy
- MAC OS (runs well)
	- Install python
	- Install pip 
	- Use pip to install opencv-python-headless (otherwise it errors) 
- Windows (Discouraged - it gave me an error, coun't run the opencv) (best option is to run a Linux server, I did on my Windows 10)
	- Install python
	- Install pip
	- Use pip to install opencv-python-headless (otherwise it errors)

#There is code to obtain images. That is written by me and already executed. You can test it and play with it if desired. There are three parts in that script which need to be executed one by one as described in the code
.
#Instructions for running the program:

#The program has already been trained and examples will be provided in the powerpoint. 

#If you wish to train (using my already created folder/code) it to observe follow these steps for one of my examples:

- Navigate to the projects folder
	- I will be using 3026 negative images and generate the same amount of positives
	- Using one of my photos for example: "Hatter.jpg"
	- Create two folders in the main project directory, one info and one data (in this case these are hatterInfo and hatterData) 
	- Below there is going to be a .vec file. Name that accordingly (in my case that is hatterpositives.vec)
	- Open terminal by means of using "cd" or by just clicking in the folder and opening the terminal from there:
	- Run: opencv_createsamples -img Hatter.jpg -bg bg.txt -info hatterInfo/hatterInfo.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -num 3026      #This will create positive images with the hatter in these images
	- Run: opencv_createsamples -info hatterInfo/hatterInfo.lst -num 3026 -w 20 -h 20 -vec hatterpositives.vec    #This will create the vector file with the positve images
	- Run: opencv_traincascade -data hatterData -vec hatterpositives.vec -bg bg.txt -numPos 2800 -numNeg 1200 -numStages 10 -w 20 -h 20         #This will start training the system and start the training process 


#To run and begin the program there is no need to train, I have trained the objects and images to the best parameters I believe: 

- To test the earbuds cascade which has been trained through 14 stages, in which the cascade trains that best for this particular example is to stage 7. After stage 7 the image is difficult to appear
	- Open terminal by means of using "cd" or by just clicking in the folder and opening the terminal from there:
	- run: python Test2.py
	- (Depending where you save the cascade.xml file, you might get an error, in the code, on the variable in which you assing the cascade, example ( german_lady_cascade = cv2.CascadeClassifier('/home...') make sure to change the directory of the particular cascade depending on where you download them)

- To test the germanlady and the hatter which are trained through 14 states and worked:
	-run: Test2_print_face.py
	- (Depending where you save the cascade.xml file, you might get an error, in the code, on the variable in which you assing the cascade, example ( german_lady_cascade = cv2.CascadeClassifier('/home...') make sure to change the directory of the particular cascade depending on where you download them)


- To test all together, earbuds, germanlady and the hatter:
	-run: Test.py 
	- (Depending where you save the cascade.xml file, you might get an error, in the code, on the variable in which you assing the cascade, example ( german_lady_cascade = cv2.CascadeClassifier('/home...') make sure to change the directory of the particular cascade depending on where you download them)



#This is how the programs are run.
#For support and sources. Most of my sources came from the opencv cascade page library. I viewed some examples from youtube as instructions for some of my code as well. 

#Sources:

[1]Sentdex, https://www.youtube.com/watch?v=-Mhy-5YNcG4&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=21. Youtube: Youtube, 2016.

[2]"Configure a Python interpreter - Help | PyCharm", Jetbrains.com, 2020. [Online]. Available: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#. [Accessed: 22- Apr- 2020].

[3]"Object Detection with Haar Cascades in Python", Medium, 2020. [Online]. Available: https://towardsdatascience.com/object-detection-with-haar-cascades-in-python-ad9e70ed50aa. [Accessed: 22- Apr- 2020].

[4]"OpenCV: Cascade Classifier", Docs.opencv.org, 2020. [Online]. Available: https://docs.opencv.org/4.2.0/db/d28/tutorial_cascade_classifier.html. [Accessed: 22- Apr- 2020].


#Author:
Antonino Abeshi 
Artificial Intelligence Class
