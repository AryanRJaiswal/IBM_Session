def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at board[row][col]

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try to place a queen in all rows
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nqueens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, return False
    return False

def solve_nqueens(n):
    # Create an empty N x N chessboard
    board = [[0] * n for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print("Solution does not exist")
        return False

    # Print the board with queens placed
    print_board(board)

def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))

if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    solve_nqueens(n)
