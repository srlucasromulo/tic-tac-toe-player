from pdi import load_images_values, load_board
from clicker import send_click, restart_click

circle_value, cross_value, blank_value = load_images_values()
board = load_board(circle_value, cross_value)
print(board)

send_click(0, 1)

restart_click()
