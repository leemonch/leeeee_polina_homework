class Tictactoe:
    def __init__(self):
        self.board = [1,2,3,4,5,6,7,8,9]
        self.current_player = "X"

    def draw_board(self):
        print(f"{self.board[0]}  {self.board[1]}  {self.board[2]}")
        print(f"{self.board[3]}  {self.board[4]}  {self.board[5]}")
        print(f"{self.board[6]}  {self.board[7]}  {self.board[8]}")

    def check_win(self):
        wins = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]
        for win in wins:
            first_index=win[0]
            second_index=win[1]
            third_index=win[2]
            if (self.board[first_index] == self.board[second_index] == self.board[third_index]):
                return True
        return False

    def play(self):
        print("начало")
        for turn in range(9):
            self.draw_board()
            move=""
            while move not in self.board:
                move=int(input(f"Ход {self.current_player}. номер клетки: "))
                if move not in self.board:
                    print("ошибка! введите свободную цифру от 1 до 9.")
            self.board[int(move)-1]=self.current_player
            if self.check_win():
                self.draw_board()
                print(f"игрок {self.current_player} победил")
                return 
            if self.current_player =="X":
                self.current_player="O"
            else:
                self.current_player="X"
        self.draw_board()
        print("Ничья!")

game=Tictactoe()
game.play()
