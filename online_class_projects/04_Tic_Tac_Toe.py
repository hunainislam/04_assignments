import time
import math

# 🎮 Tic-Tac-Toe Board
board = [" " for _ in range(9)]

def print_board():
    """Prints the Tic-Tac-Toe board."""
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print("\n")

def check_winner(player):
    """Checks if a player has won the game."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def available_moves():
    """Returns a list of available moves."""
    return [i for i, spot in enumerate(board) if spot == " "]

def player_move():
    """Handles the player's move."""
    while True:
        try:
            move = int(input("🟢 Enter your move (1-9): ")) - 1
            if move in available_moves():
                board[move] = "X"
                break
            else:
                print("❌ Invalid move! Try again.")
        except ValueError:
            print("❌ Please enter a number between 1-9.")

def ai_move():
    """AI selects the best move using the Minimax algorithm."""
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "  # Undo move
        
        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = "O"

def minimax(is_maximizing):
    """Minimax algorithm to calculate the best move for AI."""
    if check_winner("X"):
        return -1
    if check_winner("O"):
        return 1
    if not available_moves():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def main():
    print("🎲 Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner("X"):
            print("🏆 Congratulations! You Win! 🎉")
            break
        if not available_moves():
            print("⚔️ It's a Tie!")
            break
        
        print("🤖 AI is thinking...")
        time.sleep(1)  # Simulate AI thinking
        ai_move()
        print_board()
        if check_winner("O"):
            print("🤖 AI Wins! Better luck next time!")
            break
        if not available_moves():
            print("⚔️ It's a Tie!")
            break

if __name__ == "__main__":
    main()
