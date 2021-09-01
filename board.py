import numpy as np
from pdi import get_table_values


class Board:
    def __init__(self):
        self.table = np.zeros((3, 3))
        self.circle = 1
        self.cross = 2

    def load_board(self):
        self.table = \
            get_table_values(self.circle, self.cross)
