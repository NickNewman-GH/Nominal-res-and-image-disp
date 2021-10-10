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

def find_width_coords(image):
    left_x, right_x = None, None
    for line in image:
        xs = find_coords_in_line(line)
        if xs:
            if not left_x:
                left_x, right_x = xs
            else:
                left_x, right_x = min(left_x, xs[0]), max(right_x, xs[1])
    return left_x, right_x if left_x != None else None


if __name__ == "__main__":
    path = './imgs/'
    files = [file for file in listdir(path)]
    center_coords = []
    show = True

    for file in files:
        figure = open(path + file)
        real_width, sep = figure.readline()[:-1], figure.readline()[:-1]

        image = np.loadtxt(figure.readlines())

        x_l, x_r = find_width_coords(image)

        rotated_image = np.rot90(image)

        y_l, y_h = find_width_coords(rotated_image)

        center_coords.append(np.array([(x_l + x_r) / 2, (y_l + y_h) / 2]))

        if show:
            line_list = [[(x_l,x_l), (y_l, y_h)], [(x_r,x_r), (y_l, y_h)], [(x_r,x_l), (y_l, y_l)], [(x_r,x_l), (y_h, y_h)]]

            for line in line_list:
                plt.plot(*line, color = 'red')

            plt.scatter((x_l + x_r) / 2, (y_l + y_h) / 2, color = 'red')
            if len(center_coords) > 1:
                plt.scatter(*center_coords[0], color = 'red')
                plt.plot((center_coords[0][0], center_coords[1][0]), (center_coords[0][1], center_coords[1][1]), color = 'red')

            plt.imshow(image)
            plt.show()

    print('The first picture is displaced relative to the second by\nx by %f\ny by %f' % tuple(center_coords[0] - center_coords[1]))