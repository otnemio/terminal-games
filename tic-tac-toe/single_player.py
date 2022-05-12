import random
from rich import print
class TicTacToe:
    def __init__(self,lstPiece=['⬜','🟧','🟩']):
        self.board = []
        self.piece=lstPiece
        self.create_board()
        self.valid_moves = {1,2,3,4,5,6,7,8,9}
        self.gameover = False
        
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(0)
            self.board.append(row)
    
    def display_board(self):
        print()
        print('Present status of board →')
        for row in self.board:
            for item in row:
                print(self.piece[item],end='')
            print()
        print()
        self.display_help()
    
    def display_help(self):
        digit=['❶ ', '❷ ', '❸ ', '❹ ', '❺ ', '❻ ', '❼ ', '❽ ', '❾ ']
        print('Valid moves remaining →')
        for row in range(3):
            for col in range(3):
                num = (2-row)*3+col+1
                if self.board[row][col]==0:
                    print(f'[#E0E0E0]{digit[num-1]}',end='')
                elif self.board[row][col]==1:
                    print(f'[#FF9800]{digit[num-1]}',end='')
                elif self.board[row][col]==2:
                    print(f'[#7CB342]{digit[num-1]}',end='')
            print()
    
    def make_move(self,num,player):
        if num==0:
            self.gameover=True
            return True
        elif num not in self.valid_moves:
            return False
        else:
            row = 2-(num-1)//3
            col = (num-1)%3
            self.valid_moves.remove(num)
            self.board[row][col]=player
            if len(self.valid_moves)==0:
                self.gameover=True
            return True
    
        


if __name__=='__main__':
    # Check for proper display of unicode characters
    lstPiece=['⬜','🟧','🟩']
    print(lstPiece)
    if input('Do you see three properly colored squares White, Orange and Green? Please answer in yes or no ').lower().startswith('n'):
        lstPiece=['.','x','o']
        
    # player 1 is computer, player 2 is human
    t = TicTacToe(lstPiece)
    if input('Do you want to play first? Please answer in yes or no ').lower().startswith('n'):
        t.make_move(2,1)
        
    while not t.gameover:
        t.display_board()
        while not t.make_move(int(input('Enter a digit between 1 and 9 ')),2):
            continue
        if t.valid_moves:
            n = random.choice(list(t.valid_moves))
            t.make_move(n,1)

    t.display_board()