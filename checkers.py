from board import CheckersBoard
from player import Player, AIPlayer

class CheckersGame:
    def __init__(self):
        self.board = CheckersBoard()
        self.current_turn = Player.PLAYER
        self.player = Player(Player.PLAYER)
        self.ai = AIPlayer(Player.AI)

    def is_game_over(self):
        """Checks if the game is over."""
        player_pieces = sum(piece == self.player.player_type for row in self.board.board for piece in row)
        ai_pieces = sum(piece == self.ai.player_type for row in self.board.board for piece in row)
        return player_pieces == 0 or ai_pieces == 0

    def play_game(self):
        """Main game loop."""
        while not self.is_game_over():
            self.board.print_board()
            if self.current_turn == Player.PLAYER:
                print("Your turn!")
                move = self.player .get_move(self.board)
                self.board.apply_move(move)
            else:
                print("AI's turn!")
                move = self.ai.get_move(self.board)  # AI logic to get the move
                if move:
                    self.board.apply_move(move)
                else:
                    print("AI has no valid moves.")

            self.current_turn = Player.AI if self.current_turn == Player.PLAYER else Player.PLAYER

        print("Game over!")
        self.board.print_board()