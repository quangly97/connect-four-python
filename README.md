# Connect 4 Game
![connectfour1](https://user-images.githubusercontent.com/62526327/88466271-9ea22a00-ce98-11ea-9de2-ab9f74a6151b.PNG)
![connectfour2](https://user-images.githubusercontent.com/62526327/88466272-a19d1a80-ce98-11ea-9cd7-8b5f9dd0ee35.PNG)
![connectfour3](https://user-images.githubusercontent.com/62526327/88466273-a2ce4780-ce98-11ea-8351-05e7411f96ca.PNG)

## Brief
A Connect 4 game implemented with python and its pygame library.

## Methods Used
* create_board(): creates board
* draw_board(): draws board onto pygame screen/window
* column_available(board, col): checks if column is not full
* get_open_row(board, col): gets the next available row
* drop_piece(board, row, col, piece): inserts piece into the board
* connect_four(board, piece): checks if player has gotten four pieces in a row, if so, they win

## Technologies Used
* Python
* Git
* Github
* pygame
* numpy

## Sample Code
```
def connect_four(board, piece):
    for row in range(ROW - 1, -1, -1):
        for col in range(COL - 3):
            if(board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece):
                return True

    for row in range(ROW - 1, -1, -1):
        for col in range(COL):
            if(board[row][col] == piece and board[row - 1][col] == piece and board[row - 2][col] == piece and board[row - 3][col] == piece):
                return True

    for row in range(ROW - 1, ROW - 3, -1):
        for col in range(COL - 3):
            if(board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece):
                return True

    for row in range(ROW - 1, ROW - 3, -1):
        for col in range(3, COL):
            if(board[row][col] == piece and board[row - 1][col - 1] == piece and board[row - 2][col - 2] == piece and board[row - 3][col - 3] == piece):
                return True
```
