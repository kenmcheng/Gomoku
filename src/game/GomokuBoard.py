from BaseBoard import BaseBoard

class GomokuBoard(BaseBoard):

    def __init__(self, col = 15, row = 15, *args, **kwargs):
        super().__init__(col, row, args, kwargs)
        self.player = 1
    
    def move(self, col, row):
        if row < 0 or row >= self.row or col < 0 or col >=self.col:
            return 0
        if self.board[row][col] != 0:
            return 0
        self.board[row][col] = self.player
        winner = self.__judge(col, row)
        self.player = 1 if self.player == 2 else 2
        return winner

    def whosturn(self):
        return self.player

    def __judge(self, col, row) -> "winner":
        directions = [(1,0), (1,1), (0,1), (1,-1)]
        for i in range(len(directions)):
            forward = directions[i]
            winner, count = self.__search([row+forward[0], col+forward[1]], forward, 1)
            if count == 5:
                return winner
            else:
                backward = (forward[0]*-1,forward[1]*-1)
                winner, count = self.__search([row+backward[0], col+backward[1]], backward, count)
                if count == 5:
                    return winner

        return 0

    def __search(self, pos, direction, count) -> "winner, count of consecutive stones":
        if pos[0] < 0 or pos[0] >= self.row or pos[1] < 0 or pos[1] >=self.col:
            return 0, count
        if self.board[pos[0]][pos[1]] == self.player:
            count += 1
            if count == 5:
                return self.player, count
            else:
                pos[0] += direction[0]
                pos[1] += direction[1]
                return self.__search(pos, direction, count)
        else:
            return 0, count

    def print(self):
        for i in range(self.row-1, -1, -1):
            for j in range(0,self.col):
                print(self.board[i][j], end=" ")
            print()

if __name__ == "__main__":

    board = GomokuBoard(15,15)
    winner = 0
    board.print()
    while winner == 0:
        who = board.whosturn()
        user_input = input(f'Player{who}\'s turn: ')
        if user_input == "quit":
            print("Exit Gomoku...")
            break
        place = user_input.split(" ")
        winner = board.move(int(place[0]), int(place[1]))
        board.print()
        if winner > 0:
            print(f'Player{winner} won')
