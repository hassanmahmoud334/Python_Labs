import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("This method should be implemented by subclasses.")

class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                pos = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if pos < 1 or pos > 9:
                    print("Invalid position. Choose 1-9.")
                    continue
                row, col = divmod(pos - 1, 3)
                if board.get_grid[row][col] == " ":
                    return (row, col)
                else:
                    print("Cell already taken. Choose another.")
            except ValueError:
                print("Please enter a valid number.")

class ComputerPlayer(Player):
    def make_move(self, board):
        empty = [(r, c) for r in range(3) for c in range(3) if board.get_grid[r][c] == " "]
        move = random.choice(empty)
        print(f"{self.name} ({self.symbol}) chooses position {move[0]*3 + move[1] + 1}")
        return move

class Board:
    def __init__(self):
        self.__grid = [[" " for _ in range(3)] for _ in range(3)]

    @property
    def get_grid(self):
        return self.__grid

    def display(self):
        print(self)

    def update(self, position, symbol):
        row, col = position
        if self.__grid[row][col] == " ":
            self.__grid[row][col] = symbol
            return True
        return False

    def check_winner(self):
        lines = self.__grid + [list(col) for col in zip(*self.__grid)]
        lines.append([self.__grid[i][i] for i in range(3)])
        lines.append([self.__grid[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self):
        return all(cell != " " for row in self.__grid for cell in row)

    def __str__(self):
        rows = []
        for row in self.__grid:
            rows.append(" | ".join(row))
        return "\n---------\n".join(rows)

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.current_turn = 0

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        self.board.display()
        while True:
            player = self.players[self.current_turn]
            move = player.make_move(self.board)
            if self.board.update(move, player.symbol):
                self.board.display()
                winner = self.board.check_winner()
                if winner:
                    print(f"Congratulations {player.name}! You win!")
                    break
                elif self.board.is_full():
                    print("It's a draw!")
                    break
                self.switch_turns()
            else:
                print("Invalid move. Try again.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Do you want to play with a friend (1) or vs computer (2)? ")
    if mode == "1":
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        players = [HumanPlayer(name1, "X"), HumanPlayer(name2, "O")]
    else:
        name = input("Enter your name: ")
        players = [HumanPlayer(name, "X"), ComputerPlayer("Computer", "O")]
    game = Game(players)
    game.play()

if __name__ == "__main__":
    main()