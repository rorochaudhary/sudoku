# Name: Rohit Chaudhary
# Course: CS 325 - Analysis of Algorithms
# HW 8: Portfolio Project
# Date: 12/7/20
# Description: For this portion I attempted to implmement a backtracking algorithm for solving an incomplete 9x9 sudoku board. The solver takes as input a user-submitted board.txt and solves the board according to traditional Sudoku rules, outputting the result to console. board.txt contains a 9x9 multi-dimensional array containing digit values 0-9 (where 0 denotes an empty position).

def print_grid():
    """function that neatly prints grid"""
    global grid
    for row in grid:
        print(row)

def form_grid(puzzle_string):
    """function takes in a string sudoku board and converts it into a multidimensional array"""
    global grid
    for line in puzzle_string:
        str_row = list(line)
        row_len = len(str_row)
        row = []
        for i in range(row_len):
            if str_row[i].isdigit():
                row.append(int(str_row[i]))
        grid.append(row)
    print("Original Board:")
    print_grid()
    return

def possible(row, col, digit):
    """function takes a multi-dimensional array 'grid', 'row' index, 'col' index, and determines whether 'digit' can be placed grid[row][col] or not. returns True is placement is possible, otherwise returns False"""
    global grid
    # check row to see if digit is allowable
    for i in range(9):
        if grid[row][i] == digit:
            return False
    # check column to see if digit is allowable
    for i in range(9):
        if grid[i][col] == digit:
            return False
    
    # check subboxes to see if digit is allowable
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[square_row + i][square_col + j] == digit:
                return False    
    return True

def solve():
    """recursive backtracking function to solve the sudoku board"""
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1, 10):
                    if possible(row, col, digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0    
                return
    print("Solution:")
    print_grid()

# global var that is accessed by sudoku.py
grid = []

# # code to get board from board.txt
# if __name__ == "__main__":
#     with open("board.txt", 'r') as f:
#         str_board = f.readlines()
#         grid = []
#         form_grid(str_board)
#         solve()
