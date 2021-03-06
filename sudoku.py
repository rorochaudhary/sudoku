# Name: Rohit Chaudhary
# Course: CS 325 - Analysis of Algorithms
# HW 8: Portfolio Project
# Date: 12/7/20
# Description: User interaction management for the Sudoku program, which allows for a user to input a 9x9 sudoku tile entry that he/she completed for verification or provide a sudoku problem for the solver portion of this program to complete and output.

import sys
import sudoku_verifier as Verifier
import sudoku_solver as Solver

def input_error():
    """error resolution during verification or solution stage, allowing user to retry or exit"""
    err_prompt1 = "Sorry, there may have been an error with the input of the board, please try again."
    err_prompt2 = "To try again, press y or Y. If you would like to quit, press q or Q: "
    err_keys = {"q": 0, "Q": 0, "y": 1, "Y": 1}

    print(err_prompt1)
    user_key = input(err_prompt2)

    while user_key not in err_keys:
        user_key = input(err_prompt2)

    if err_keys[user_key] == 0:
        print("Goodbye!")
        sys.exit()
    elif err_keys[user_key] == 1:
        return

def gather_input(prompt):
    """gathers sudoku board from user line by line. takes a prompt string as input"""
    row_prompt = "Row {}: "
    print(prompt)

    count = 0
    board = []
    while count < 9:
        row = []
        count += 1
        line = list(input(row_prompt.format(count)))
        row_len = len(line)
        for i in range(row_len):
            if line[i].isdigit():
                row.append(int(line[i]))
        board.append(row)
    
    # print("your board:\n{}".format(board))
    return board

def sudoku_verify():
    """calls verification methods"""
    verify_prompt1 = "Let's verify your solution! Please enter your row line by line - comma separated in the format of num1, num2, num3, ..., num9."
    success_str = "Success! Your board is a correct solution."
    fail_str = "Sorry, your board is not a correct solution."

    while True:
        try:
            board = gather_input(verify_prompt1)

            # verify
            if Verifier.check_solution(board) == True:
                print(success_str)
                return True
            else:
                print(fail_str)
                return False
        except:
            input_error()

def sudoku_solve():
    """calls solution methods"""
    solve_prompt1 = "Let's solve your board! Please enter your row line by line - comma separated in the format of num1, num2, num3, ..., num9. Use 0 to denote an empty sudoku square."
    grid_prompt = "The board you gave:"

    while True:
        try:
            board = gather_input(solve_prompt1)
            Solver.grid = board
            print(grid_prompt)
            Solver.print_grid()
            Solver.solve()
            print("Goodbye!")
            return
        except:
            input_error()

def load_board():
    """gives user a sudoku board and then allows user input their solution to verify"""
    instructions_str = "\nAwesome!\n"\
                       "Goal: The 9x9 board needs to be filled such that each row, column, and each of the nine 3x3 subboxes contain the digits 1-9 exactly once.\n"\
                       "Your puzzle (the 0s need to be replaced with digits 1-9!):"

    with open('board.txt', 'r+') as f:
        game = []
        for line in f.readlines():
            str_row = list(line)
            row_len = len(str_row)
            row = []
            for i in range(row_len):
                if str_row[i].isdigit():
                    row.append(int(str_row[i]))
            game.append(row)
        print(instructions_str)
        print_board(game)
        done_board(game)

def done_board(board):
    """helper function to load_board, determines whether user wants to verify the board or give a solution"""
    next_str = "\nWhen you are done and want to verify your solution, press v (or V). "\
                "If you give up and want the solution to the board, press s (or S) to start the solver and input the board row by row."\
                "\nTo quit, press q (or Q): "
    err_input_str = "Sorry, I did not recognize that input."
    board_keys = {"q": 0, "Q": 0, "s": 1, "S": 1, "v": 2, "V": 2}

    user_input = input(next_str)
    while user_input not in board_keys:
        print(err_input_str)
        user_input = input(next_str)
    
    if board_keys[user_input] == 0:
        print("Goodbye!")
        sys.exit()
    elif board_keys[user_input] == 1:
        sudoku_solve()
    else:
        sudoku_verify()

def print_board(board):
    for row in board:
        print(row)

if __name__ == "__main__":
    greeting_str1 = "Welcome to the Sudoku Verifier/Solver!\n"
    greeting_str2 = "Written by Rohit Chaudhary\n"
    method_prompt1 = "If you would like to input a sudoku board solution for me to verify, press v (or V).\n"
    method_prompt2 = "If you want to input a sudoku board problem to be solved by me, press s (or S).\n"
    method_prompt3 = "If you would like to try solve the board I have for you and I can verify it, press b (or B): "
    allowed_input = {"q": 0, "Q": 0, "v": 1, "V": 1, "s": 2, "S": 2, "b": 3, "B": 3}
    exit_input = {"q", "Q"}
    error_str1 = "Sorry, I did not recognize that. Please, try again. To quit, press q or Q"

    # greetings, determine whether user wants to solve or verify
    print(greeting_str1 + greeting_str2)
    user_input = input(method_prompt1 + method_prompt2 + method_prompt3)
    while user_input not in allowed_input:
        print(error_str1)
        user_input = input(method_prompt1 + method_prompt2 + method_prompt3)
    
    # check for quit
    if user_input in exit_input:
        print("Goodbye!")
        sys.exit()

    # run appropriate module based on input
    if allowed_input[user_input] == 1:
        sudoku_verify()
    elif allowed_input[user_input] == 2:
        sudoku_solve()
    elif allowed_input[user_input] == 3:
        load_board()
