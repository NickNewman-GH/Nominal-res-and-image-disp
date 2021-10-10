#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from os import listdir

def find_item(arr, item, rotation = 1):
    settings = {-1 : [len(arr)-1, 0, -1], 1 : [len(arr)]}
    for i in range(*settings[rotation]):
        if arr[i] == item:
            return i
    return None

def find_coords_in_line(line):
    begin_coord = find_item(line, 1)
    end_coord = find_item(line, 1, -1)
    return (begin_coord, end_coord) if begin_coord else begin_coord

def find_pix_width(image):
    left_x, right_x = None, None
    for line in image:
        xs = find_coords_in_line(line)
        if xs:
            if not left_x:
                left_x, right_x = xs
            else:
                left_x, right_x = min(left_x, xs[0]), max(right_x, xs[1])
    return right_x - left_x + 1 if left_x != None else None


if __name__ == "__main__":
    path = './figures/'

    files = [file for file in listdir(path)]

    for file in files:
        figure = open(path + file)
        real_width, sep = figure.readline()[:-1], figure.readline()[:-1]

        image = np.loadtxt(figure.readlines(), dtype = 'uint')

        pix_width = find_pix_width(image)

        print(float(real_width)/pix_width if pix_width else 0)

        #plt.imshow(image)
        #plt.show()