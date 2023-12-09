class Knight:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, next_col, next_row):
        next_col = ord(next_col) - ord('a')
        prev_col = ord(self.col) - ord('a')
        x_move = abs(next_row - self.row)
        y_move = abs(next_col - prev_col)
        if (x_move == 1 and y_move == 2) or (x_move == 2 and y_move == 1):
            return True
        else:
            return False

    def move_to(self, next_col, next_row):
        if self.can_move(next_col, next_row):
            self.col = next_col
            self.row = next_row

    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        X1 = 8 - self.row
        Y1 = ord(self.col) - ord('a')
        board[X1][Y1] = 'N'

        for i in range(8):
              for j in range(8):
                  if (abs(Y1 - i) == 2 and abs(X1 - j) == 1) or (abs(Y1 - i) == 1 and abs(X1 - j) == 2):
                      board[j][i] = '*'

        for i in board:
            print(*i, sep='')
