import IPython.display as ip
import random
class Board():
    def __init__(self):
        self.cells = [' ' for i in range(0,10)]
    def pt(self):
        print(self.cells)
    def display(self):
        print(f'{self.cells[1]} |{self.cells[2]} |{self.cells[3]} ')
        print(' ------')
        print(f'{self.cells[4]} |{self.cells[5]} |{self.cells[6]} ')
        print(' ------')
        print(f'{self.cells[7]} |{self.cells[8]} |{self.cells[9]} ')
        print('\n')
    def update_cell(self,cell_no,playr):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = playr
    def winner(self,plyr):
        return ((self.cells[1] == self.cells[2] == self.cells[3] == plyr) or (self.cells[4] == self.cells[5] == self.cells[6] == plyr)
               or (self.cells[7] == self.cells[8] == self.cells[9] == plyr) or
               (self.cells[7] == self.cells[5] == self.cells[3] == plyr) or
               (self.cells[1] == self.cells[5] == self.cells[9] == plyr))
    def reset(self):
        self.cells = [' ' for i in range(0,10)]
    def is_tie(self):
        cell_used = 0
        for cell in self.cells:
            if cell != " ":
                cell_used +=1
            if cell_used == 9:
                return True
        return False
    def ai_move(self,playr):
        for i in range(1,10):
            r= random.randint(1,9)
            if self.cells[r] == ' ':
                return r
    def print_head(self):
        ip.clear_output()
        print('Welcome to Tic tac toe')
        self.reset()
        self.display()
def main():
    board.print_head()
    while True:
        
        x_choice = int(input("Enter From  1 to 9 For X :"))
        while board.cells[x_choice] != " " :
            print(f'{x_choice} is full try other number')
            x_choice = int(input("Enter From  1 to 9 For X :"))
        board.update_cell(x_choice,'X')#' * * \n  * \n * * '
        board.display()
        if board.winner('X'):
            print("X is a Winner")
            play_again = input("Would You like to Play again? (Y/N) :").upper()
            if play_again == 'Y':
                board.reset()
                continue
            else:
                break
        if board.is_tie():
            print("Game is Tie")
            play_again = input("Would You like to Play again? (Y/N) :").upper()
            if play_again == 'Y':
                board.reset()
                continue
            else:
                break    
        o_choice = board.ai_move('O')
        board.update_cell(o_choice,'O')#' * * \n  * \n * * '
        board.display()
        if board.winner('O'):
            print("O is a Winner")
            play_again = input("Would You like to Play again? (Y/N) :").upper()
            if play_again == 'Y':
                board.reset()
                continue
            else:
                break
        if board.is_tie():
            print("Game is Tie")
            play_again = input("Would You like to Play again? (Y/N) :").upper()
            if play_again == 'Y':
                board.reset()
                continue
            else:
                break
board = Board()
main()
