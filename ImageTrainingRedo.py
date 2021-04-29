"""
Created by Antonino Abeshi
CS455 Artificial Intelligence Class
Due 04/25/2020

"""

import urllib.request
import cv2
import numpy as np
import os

"""
Below we will add negative images from the image-net website. I have added three links because I kept adding images. 
I have added bananas images to start, then dog images, and then cars with people images. The way these images are added 
are by urls. Basically we have a huge collection of urls with each image, that gets transferred into our negative image
folder.
Each time images are added we update the pic_num. This starts the next number of the images and continues
from there. 

Now these go in order.
First we run the store_raw_images() in order to store the raw images, resize them, modify them and grayscale them
Second we run the find blanks. This simply elimantes any bad images. Sometimes from the urls, there are images that 
are just blank with nothing in them.
Third we run create_pos_n_neg() which runs all the files and creates descriptions of them, saving them into the 
bg.txt
CAUTION (You cannot run all at once, they need to be run one by one in order to be effective)
"""


def store_raw_images():
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07753592' # bananas
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02109961' # dogs
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02918964'  # cars with people
    neg_images_url = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    # pic_num = 1
    # pic_num = 1059
    pic_num = 2116

    for i in neg_images_url.split('\n'):  # urls that we just visited, we split them by a newline and we got
        # all of them organized
        try:
            print(i)  # we are printing the link that we are visiting
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + '.jpg')  # we are retrieving the url and the we are
            # saving the raw image both color and various sizes to the # neg directory
            img = cv2.imread("neg/" + str(pic_num) + '.jpg', cv2.IMREAD_GRAYSCALE)  # so basically we are trying to
            # modify all the images with cv2, basically by getting the image ,reading it and putting it in gray scale
            resized_image = cv2.resize(img, (100, 100))  # negative images mostly for now we are
            # resizing all of the mto 100 by 100
            cv2.imwrite("neg/" + str(pic_num) + '.jpg', resized_image)  # and now we write the images into the
            # same directory which is the neg, resized
            pic_num += 1  # we use this as a counter to get to the other images

        except Exception as e:  # a lot of these are going to fail so we just print this:
            print(str(e))


# store_raw_images()

# --------------------------------------------------------------------------------------------------------------

def find_blanks():  # trying to find the blank images on the folder
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for blank in os.listdir('BadImages'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)  # file type is the directory path
                    blank = cv2.imread('Blank_files/' + str(blank))
                    question = cv2.imread(current_image_path)

                    if blank.shape == question.shape and not (np.bitwise_xor(blank, question).any()):  # if same
                        # dimensions xor either one or the other but not both.
                        print('Blank Image')
                        print(current_image_path)
                        os.remove(current_image_path)  # we remove this image if we find the blank one

                except Exception as e:
                    print(str(e))


# find_blanks()

# -----------------------------------------------------------------------------------------------------------------

# Create description files

def create_pos_n_neg():
    for file_type in ['neg']:  # for this path in neg

        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'  # in the negative file this is all we have,
                # the paths of these negative images
                with open('bg.txt', 'a') as f:
                    f.write(line)


            # positive file_types now

            elif file_type == 'pos':
                line = file_type + '/' + img + '1 0 0 50 50 \n'  # the file types of positives,
                # how many objects, rectangle location of the objects
                with open('info.dat', 'a') as f:
                    f.write(line)

# create_pos_n_neg() # runs all the files


# ----------------------------------------------------------------------------------------------------------------
