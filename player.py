from board import Board
from pdi import load_images_values, check_winner
from clicker import send_click, restart_click
from ai import play
import time

board = Board()
player = board.cross
win = 0
lose = 0
draw = 0

load_images_values()

while True:

    print('\nloading board...')
    board.load_board()

    print('getting position...')
    position = play(board.table)

    print('sending click...')
    send_click(position[0], position[1])

    print('\nchecking winner...')
    time.sleep(1)
    winner = check_winner()
    if winner:
        if winner == 3:
            print('its a draw!!!')
            draw += 1
        elif winner == player:
            print('oh yes!!!')
            win += 1
        else:
            print('oh no =/')
            lose += 1

        print(f'Balance: win {win}, lose {lose}, draw {draw}')

    else:
        print('the game is still running...')

        # op = None
        # while op != 'Y' and op != 'N':
        #     op = input('Play again? (y/n) _> ').upper()
        # if op == 'N':
        #     break

        restart_click()
