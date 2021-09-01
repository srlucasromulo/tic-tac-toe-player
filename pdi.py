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


def load_images_values():
    global circle_value, cross_value, blank_value, \
    circle_winner, cross_winner, draw

    circle_value = cv2.imread('./images/circle.jpg')
    circle_value = np.array(circle_value)

    cross_value = cv2.imread('./images/cross.jpg')
    cross_value = np.array(cross_value)

    blank_value = cv2.imread('./images/blank.jpg')
    blank_value = np.array(blank_value)

    circle_winner = cv2.imread('./images/circle_winner.jpg')
    circle_winner = np.array(circle_winner)

    cross_winner = cv2.imread('./images/cross_winner.jpg')
    cross_winner = np.array(cross_winner)

    draw = cv2.imread('./images/draw.jpg')
    draw = np.array(draw)


def compare_images(image0, image1):
    comparsion = image0 == image1
    comparsion = comparsion.all()
    return comparsion


def get_table_values(circle, cross):
    table = np.zeros((3, 3))
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
                table[i, j] = circle
            elif compare_images(current, cross_value):
                table[i, j] = cross
            else:
                table[i, j] = 0

    return table


def check_winner():
    area = (380, 450, 630, 630)
    img = pyscreenshot.grab(bbox=area)
    img_np = np.array(img)
    cv2.imwrite('./images/winner.jpg', img_np)

    winner = cv2.imread('./images/winner.jpg')
    winner = np.array(winner)

    if compare_images(winner, circle_winner):
        return 1
    if compare_images(winner, cross_winner):
        return 2
    if compare_images(winner, draw):
        return 3
    return 0
