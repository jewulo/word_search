# https://youtube.com/shorts/gyR8BD_TUHA

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def __init__(self):
        self.board = None
        self.COLS = None
        self.ROWS = None

    def exist(self, _board, word):
        self.ROWS = len(_board)
        self.COLS = len(_board[0])
        self.board = _board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

        ret = False
        self.board[row][col] = '#'

        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            if ret: break

        self.board[row][col] = suffix[0]
        return ret


def do_work(board, word):
    sol = Solution()
    if sol.exist(board, word):
        print(word + " Found")
    else:
        print(word + " Not Found")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    do_work(board, "ABCCE")
    do_work(board, "ABCCEFQ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
