'''
    Tic-Tac-Toe is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.
'''

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "X" if self.current_player == "O" else "O"
        else:
            print("Invalid move. The position is already occupied.")

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]
        return None

    def check_draw(self):
        return " " not in self.board

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.print_board()
            position = int(input(f"{self.current_player}, enter your move (0-8): "))
            if position < 0 or position > 8:
                print("Invalid position. Please choose a position between 0 and 8.")
                continue
            self.make_move(position)
            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"{winner} wins!")
                break
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
