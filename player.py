class Player:
    def __init__(self, player_type):
        self.player_type = player_type

    def get_move(self, board):
        """Gets a valid move from the human player."""
        while True:
            try:
                start_row = int(input("Enter start row (0-7): "))
                start_col = int(input("Enter start column (0-7): "))
                end_row = int(input("Enter end row (0-7): "))
                end_col = int(input("Enter end column (0-7): "))
                
                move = ((start_row, start_col), (end_row, end_col))
                
                if board.is_valid_move((start_row, start_col), (end_row, end_col)):
                    return move
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter integers between 0 and 7.")


class AIPlayer(Player):
    def __init__(self, player_type):
        super().__init__(player_type)
        self.opponent_type = Player.PLAYER if player_type == Player.AI else Player.AI

    def get_move(self, board):
        """Determines the best move for the AI player using the Minimax algorithm with Alpha-Beta pruning."""
        best_move = None
        best_score = float('-inf')

        for row in range(board.BOARD_SIZE):
            for col in range(board.BOARD_SIZE):
                if board.board[row][col] == self.player_type:
                    for r in range(board.BOARD_SIZE):
                        for c in range(board.BOARD_SIZE):
                            if board.is_valid_move((row, col), (r, c)):
                                # Simulate the move
                                original_piece = board.board[r][c]
                                board.board[r][c] = self.player_type
                                board.board[row][col] = board.EMPTY

                                # Evaluate the move using minimax
                                score = self.minimax(board, 3, float('-inf'), float('inf'), False)

                                # Undo the move
                                board.board[row][col] = self.player_type
                                board.board[r][c] = original_piece

                                # Update the best move if the score is higher
                                if score > best_score:
                                    best_score = score
                                    best_move = ((row, col), (r, c))

        return best_move if best_move else None

    def minimax(self, board, depth, alpha, beta, is_maximizing):
        """Minimax algorithm with Alpha-Beta pruning."""
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if is_maximizing:
            max_eval = float('-inf')
            for row in range(board.BOARD_SIZE):
                for col in range(board.BOARD_SIZE):
                    if board.board[row][col] == self.player_type:
                        for r in range(board.BOARD_SIZE):
                            for c in range(board.BOARD_SIZE):
                                if board.is_valid_move((row, col), (r, c)):
                                    # Simulate the move
                                    original_piece = board.board[r][c]
                                    board.board[r][c] = self.player_type
                                    board.board[row][col] = board.EMPTY

                                    eval = self.minimax(board, depth - 1, alpha, beta, False)

                                    # Undo the move
                                    board.board[row][col] = self.player_type
                                    board.board[r][c] = original_piece

                                    max_eval = max(max_eval, eval)
                                    alpha = max(alpha, eval)
                                    if beta <= alpha:
                                        break
            return max_eval
        else:
            min_eval = float('inf')
            for row in range(board.BOARD_SIZE):
                for col in range(board.BOARD_SIZE):
                    if board.board[row][col] == self.opponent_type:
                        for r in range(board.BOARD_SIZE):
                            for c in range(board.BOARD_SIZE):
                                if board.is_valid_move((row, col), (r, c)):
                                    # Simulate the move
                                    original_piece = board.board[r][c]
                                    board.board[r][c] = self.opponent_type
                                    board.board[row][col] = board.EMPTY

                                    eval = self.minimax(board, depth - 1, alpha, beta, True)

                                    # Undo the move
                                    board.board[row][col] = self.opponent_type
                                    board.board[r][c] = original_piece

                                    min_eval = min(min_eval, eval)
                                    beta = min(beta, eval)
                                    if beta <= alpha:
                                        break return min_eval

    def evaluate_board(self, board):
        """Evaluate the board state for the AI's perspective."""
        score = 0
        for row in range(board.BOARD_SIZE):
            for col in range(board.BOARD_SIZE):
                if board.board[row][col] == self.player_type:
                    score += 1  # Add points for each piece
                elif board.board[row][col] == self.opponent_type:
                    score -= 1  # Subtract points for opponent's pieces
        return score

    def opponent_type(self):
        """Returns the opponent's player type."""
        return Player.PLAYER if self.player_type == Player.AI else Player.AI