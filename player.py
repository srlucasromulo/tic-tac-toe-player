from pdi import load_images_values, load_board
from clicker import send_click, restart_click
from ai import winning, play

circle_value, cross_value, blank_value = load_images_values()

while True:
    board = load_board(circle_value, cross_value, blank_value)
    print(f'board \n{board}')
    position = play(board)
    # print(position)
    send_click(position[0], position[1])
