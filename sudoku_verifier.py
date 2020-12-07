# Name: Rohit Chaudhary
# Course: CS 325 - Analysis of Algorithms
# HW 8: Portfolio Project
# Date: 12/7/20
# Description: For this project I chose to implement a 9x9 Sudoku solution verifier. The verifier takes as input a user-submitted solution.txt and determines whether solution.txt is a valid solution certifiate according to the rules of Sudoku. solution.py contains a 9x9 multi-dimensional array containing digit values 0-9 (where 0 denotes an empty position).

def check_solution(certificate):
    """iterates over certificate and determines whether certificate is a valid solution according to Sudoku rules: each row, each column, and each non-overlapping 3x3 grid must contain values between 1 and 9. returns True if certificate is a valid solution or False otherwise"""

    # check for 9x9 size solution
    r = len(certificate)
    if r != 9:
        return False
    else:
        for i in range(r):
            if len(certificate[i]) != 9:
                return False

    # verify according to sudoku rules
    if check_rows(certificate) and check_columns(certificate) and check_subboxes(certificate):
        return True
    else:
        return False
    
def check_rows(certificate):
    """intermediate function called by check_solution in order to determine whether each row of sudoku solution contains digits 1-9 exactly once"""
    r = len(certificate)
    
    for i in range(r):
        row = set(certificate[i])
        if sum(row) != 45 or len(row) != 9:
            return False

    return True

def check_columns(certificate):
    """intermediate function called by check_solution in order to determine whether each column of sudoku solution contains digits 1-9 exactly once"""
    r = len(certificate)
    
    # list of sets, each set is a column
    col_grid = [set() for x in range(r)]
    for i in range(r):
        for j in range(r):
            col_grid[j].add(certificate[i][j])
    
    # verify columns
    for i in range(r):
        if sum(col_grid[i]) != 45 or len(col_grid[i]) != 9:
            return False
    
    return True

def check_subboxes(certificate):
    """intermediate function called by check_solution in order to determine whether each 3x3 sub-box of the sudoku solution contains digits 1-9 exactly once"""
    r = len(certificate)
    boxes = [[set() for k in range(3)] for l in range(3)]

    # get the subboxes
    for i in range(r):
        for j in range(r):
            row = i // 3
            col = j // 3
            boxes[row][col].add(certificate[i][j])

    # verify subboxes
    for i in range(3):
        for j in range(3):
            if sum(boxes[i][j]) != 45 or len(boxes[i][j]) != 9:
                return False

    return True

# # code below grabs board in solution.txt and verifies the solution
# if __name__ == "__main__":
#     with open('solution.txt', 'r') as f:
#         board = []
#         for line in f.readlines():
#             str_row = list(line)
#             row_len = len(str_row)
#             row = []
#             for i in range(row_len):
#                 if str_row[i].isdigit():
#                     row.append(int(str_row[i]))
#             board.append(row)

#         decision = check_solution(board)
#         print("decision:", decision)
