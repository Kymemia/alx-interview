#!/usr/bin/python3

"""
this is a program that solves the N queens problem
"""
import sys


def is_safe(board, row, col, n):
    """
    method definition that checks if a queen
    can be replaced at a certain position on the board
    """
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_n_queens(n, row, board):
    """
    method definition that attempts
    to solve n queens recursively
    """
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, row + 1, board)


def print_board(board):
    """
    method definition to print the board's current state
    """
    n = len(board)
    solution = []
    for row in range(n):
        solution.append([row, board[row]])
    print(solution)


def main():
    """
    main program
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve_n_queens(n, 0, board)


if __name__ == "__main__":
    main()
