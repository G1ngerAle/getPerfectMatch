from random import random
import pandas as pd
import cv2
import os
import imageio
import argparse
import matplotlib
import numpy as np




class UserPackage:
    def mais1(path0):
        # create a dataframe
        image_list = pd.DataFrame([], columns=["A"])
        Red_list = pd.DataFrame([], columns=["A"])
        Green_list = pd.DataFrame([], columns=["A"])
        Blue_list = pd.DataFrame([], columns=["A"])

        # folder path
        dir_path = (path0)

        # list to store files
        res = []

        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)
        # read an image in loop
        for i in range(len(res)):
            path_list = res[i]
            image_list.append(path_list)
            i += 1
        # take the image from the list
        for j in range(len(image_list.index)):
            # Read RGB image
            img = cv2.imread(image_list[j])
            image = cv2.cvtColor(img, cv2.IMREAD_COLOR)
            R = image[150, 100, 0]
            G = image[150, 100, 1]
            B = image[150, 100, 2]
            if R >= G & R >= B:
                Red_list.append(image_list[j])
            elif G >= R & G >= B:
                Green_list.append(image_list[j])
            elif B >= R & B >= G:
                Blue_list.append(image_list[j])


class UserInput:
    def mais2(path1):
        pic = cv2.imread(path1, cv2.IMREAD_COLOR)
        R = pic[150, 100, 0]
        G = pic[150, 100, 1]
        B = pic[150, 100, 2]
        if R >= G & R >= B:
            path_2 = UserPackage.mais1.Red_list[random.randint in range(len(UserPackage.mais1.Red_list))]
        elif G >= R & G >= B:
            path_2 = UserPackage.mais1.Green_list[random.randint in range(len(UserPackage.mais1.Green_list))]
        elif B >= R & B >= G:
            path_2 = UserPackage.mais1.Blue_list[random.randint in range(len(UserPackage.mais1.Blue_list))]
        output = cv2.imread(path_2, cv2.IMREAD_COLOR)
        cv2.imshow(output, output)


def image_pack(path):
    dirpath = path
    list = []

    # Iterate directory
    for path in os.listdir(dirpath):
        # check if current path is a file
        if os.path.isfile(os.path.join(dirpath, path)):
            list.append(path)

    path_output = list[random in range(len(list))]
    image_output = cv2.imread('/Users/henry/Desktop/MAIS Hacks/' + path_output)
    window_name = "image"
    cv2.imshow(window_name, image_output)
    # waits for user to press any key
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


path_3 = input("Input your path here: ")
path_4 = input("Input the path of picture you want to match: ")

image_pack(path_3)
