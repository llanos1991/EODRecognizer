##https://gist.github.com/Amir22010/a99f18ca19112bc7db0872a36a03a1ec
##https://www.codetd.com/es/article/12698667

import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join

dirs = ['annotation','monedero', 'images','monedero']
classes = ['monedero']

def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '/*.jpg'):
        image_list.append(filename)

    return image_list


print(os.getcwd())
##print(getImagesInDir(dir_path))
