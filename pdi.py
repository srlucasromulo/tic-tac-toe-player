import numpy as np
import cv2
import pyscreenshot

size = 48
delta = 188
x0 = 412
y0 = 445
x1 = x0 + delta
y1 = y0 + delta
space_between = (delta - 3 * size) / 2

board = np.zeros((3, 3))
circle = 1
cross = 2


def load_images_values():
    circle_value = cv2.imread('./images/circle.jpg')
    circle_value = np.array(circle_value)

    cross_value = cv2.imread('./images/cross.jpg')
    cross_value = np.array(cross_value)

    blank_value = cv2.imread('./images/blank.jpg')
    blank_value = np.array(blank_value)

    return circle_value, cross_value, blank_value


def compare_images(image0, image1):
    comparsion = image0 == image1
    comparsion = comparsion.all()
    return comparsion


def load_board(circle_value, cross_value):
    for i in range(3):
        for j in range(3):
            x0_ = int(x0 + j * (size + space_between))
            y0_ = int(y0 + i * (size + space_between))
            x1_ = (x0_ + size)
            y1_ = (y0_ + size)
            area = (x0_, y0_, x1_, y1_)
            img = pyscreenshot.grab(bbox=area)
            img_np = np.array(img)
            # cv2.imshow(f'i {i} j {j}', img_np)

            cv2.imwrite('./images/current.jpg', img_np)
            current = cv2.imread('./images/current.jpg')
            current = np.array(current)

            if compare_images(current, circle_value):
                board[i, j] = circle
            elif compare_images(current, cross_value):
                board[i, j] = cross

    return board
