from pdi import load_images_values, load_board

circle_value, cross_value, blank_value = load_images_values()
board = load_board(circle_value, cross_value)
print(board)
