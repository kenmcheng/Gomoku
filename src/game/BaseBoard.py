
class BaseBoard:

    def __init__(self, col, row, *args, **kwargs):
       self.col = col
       self.row = row
       self.board = [[0] * col for i in range(row)]

    def size(self):
        return self.col, self.row

    def move(self, col, row) -> int:
        pass

    def whosturn(self) -> int:
        pass

    def print(self):
        for i in range(0,self.row):
            for j in range(0,self.col):
                print(self.board[i][j], end=" ")
            
            print()





if __name__ == "__main__":
    board = base_board(3,4)
    board.print()
