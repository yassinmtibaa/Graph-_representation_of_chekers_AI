class CheckersBoard:
    EMPTY = 0
    PLAYER = 1
    AI = 2
    BOARD_SIZE = 8

    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        """Sets up the initial board configuration."""
        board = [[self.EMPTY for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        for row in range(3):
            for col in range(self.BOARD_SIZE):
                if (row + col) % 2 == 1:
                    board[row][col] = self.PLAYER
        for row in range(5, self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if (row + col) % 2 == 1:
                    board[row][col] = self.AI
        return board

    def print_board(self):
        """Prints the current state of the board."""
        for row in self.board:
            print(" ".join(str(piece) for piece in row))
        print()

    def is_valid_move(self, start, end):
        """Checks if a move is valid."""
        start_row, start_col = start
        end_row, end_col = end
        if (0 <= start_row < self.BOARD_SIZE and
            0 <= start_col < self.BOARD_SIZE and
            0 <= end_row < self.BOARD_SIZE and
            0 <= end_col < self.BOARD_SIZE):
            if self.board[start_row][start_col] == self.PLAYER or self.board[start_row][start_col] == self.AI:
                if self.board[end_row][end_col] == self.EMPTY:
                    return True
        return False

    def apply_move(self, move):
        """Applies a move to the board."""
        start, end = move
        start_row, start_col = start
        end_row, end_col = end
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = self.EMPTY