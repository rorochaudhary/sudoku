# sudoku
## Solution verifier and checker for the classic 9x9 sudoku game. Includes one playable board.

### Goal:
End up with a 9x9 grid of numbers such that each row, column, and non-overlapping 3x3 subbox does contains exactly the digits 1-9.

### Instructions on running sudoku:
1. Clone this repository locally. All files should be in the same folder location with one another.
2. Make sure you have Python 3.x installed.
3. Navigate via command line to your local copy of sudoku and execute 'python3 sudoku.py'
4. Follow the instructions of the game, summarized here:
    + #### For verifying your completed sudoku board:
        - Key press 'v' or 'V' when prompted
        - Enter your board one row at a time (as prompted), separating each number with a comma
            - example row: 1, 2, 3, 4, 5, 6, 7, 8, 9
        + After the 9th row is entered, sudoku.py will verify your solution!
    + #### For solving an incomplete sudoku board:
        - Key press 's' or 'S' when prompted
        - Just like the verifier, enter your board one comma-separated row at a time however empty spaces are replaced with a 0 (must be 0!)
        - After the 9th row is entered, sudoku.py will print the solved board to the console/terminal!
    + #### For playing the board available within this program:
        - Key press 'b' or 'B' when prompted
        - The board will be displayed where you can attempt to solve it on your own.
        - When you believe you have a solution, press 'v' or 'V' to enter the board row by row for vertification
        - If you quit and want the solution instead, press 's' or 'S' to enter the board row by row for the solution

    + For demonstration purposes, solution.txt and board.txt contain a single solved and a single unsolved sudoku board (the board which can be played within the program) which you can use to input into their respective verifier/solver capabilites.