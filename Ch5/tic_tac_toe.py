# board = [["-"] * 3] * 3  # Create a board
board = [["-"] * 3 for _ in range(3)]

board[1][0] = "X"        # Make a move

# Print board to screen
for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")
