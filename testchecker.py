def check_board(board):
    correct = [i+1 for i in range(9)]
    for r in range(9):
        if (sorted(board[r]) != correct):
            return False
    for c in range(9):
        if (sorted(board[i][c] for i in range(9)) != correct):
            return False
    for mr in range(3):
        for mc in range(3):
            if sorted([board[3*mr+i][3*mc+j] for j in range(3) for i in range(3)])!= correct:
                return False
    return True


print(check_board([[9, 1, 4, 2, 3, 7, 5, 6, 8], [6, 3, 2, 1, 5, 8, 4, 9, 7], [7, 8, 5, 4, 6, 9, 2, 1, 3], [1, 4, 3, 5, 7, 6, 9, 8, 2], [5, 9, 7, 8, 1, 2, 3, 4, 6], [8, 6, 2, 3, 9, 4, 1, 7, 5], [3, 5, 8, 7, 4, 1, 6, 2, 9], [4, 2, 9, 6, 8, 3, 7, 5, 1], [6, 7, 1, 9, 2, 5, 8, 3, 4]]))
