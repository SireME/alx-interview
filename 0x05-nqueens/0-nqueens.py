#!/usr/bin/python3
""" This module solves the N queens problem"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """
    Utility function to solve N Queens problem.

    Args:
        board (list): The chessboard.
        col (int): The current column.
        N (int): The size of the board.

    Returns:
        bool: True if all queens are placed successfully, False otherwise.
    """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0

    return res


def solve_nqueens(N):
    """
    Solve N Queens problem.

    Args:
        N (int): The size of the board.

    Returns:
        bool: True if at least one solution is found, False otherwise.
    """
    if not isinstance(N, int):
        print("N must be a number")
        return False
    if N < 4:
        print("N must be at least 4")
        return False

    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("No solution found")
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if not solve_nqueens(N):
        sys.exit(1)
