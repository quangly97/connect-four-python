import pygame
import numpy as np
import sys
import math

ROW = 6
COL = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def create_board():
    return np.zeros((ROW, COL))

def column_available(board, col):
    return board[0][col] == 0

def get_open_row(board, col):
    for row in range(ROW - 1, -1, -1):
        if(board[row][col] == 0):
            return row

def drop_piece(board, row, col, piece):
    board[row][col] = piece

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

def draw_board(screen, board):
    for row in range(ROW):
        for col in range(COL):
            pygame.draw.rect(screen, BLUE, (col*PXLSIZE, row*PXLSIZE + PXLSIZE, PXLSIZE, PXLSIZE))
            pygame.draw.circle(screen, BLACK, (col*PXLSIZE + PXLSIZE//2, row*PXLSIZE + PXLSIZE + PXLSIZE//2), RADIUS)

    for row in range(ROW):
        for col in range(COL):
            if(board[row][col] == 1):
                pygame.draw.circle(screen, RED, (col*PXLSIZE + PXLSIZE//2, row*PXLSIZE + PXLSIZE + PXLSIZE//2), RADIUS)
            elif(board[row][col] == 2):
                pygame.draw.circle(screen, YELLOW, (col*PXLSIZE + PXLSIZE//2, row*PXLSIZE + PXLSIZE + PXLSIZE//2), RADIUS)


turn = 0
game_over = False

PXLSIZE = 100
height = (ROW + 1)*PXLSIZE
width = COL*PXLSIZE
RADIUS = PXLSIZE//2 - 5
screen = pygame.display.set_mode((width, height))

board = create_board()
draw_board(screen, board)

pygame.display.update()
pygame.init()

game_over_message = pygame.font.SysFont("arial", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, PXLSIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, PXLSIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, PXLSIZE//2), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, PXLSIZE))
            if turn == 0:
                get_value = event.pos[0]
                col = math.floor(event.pos[0])//PXLSIZE
                
                if column_available(board, col):
                    row = get_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if connect_four(board, 1):
                        label = game_over_message.render("PLAYER 1 WINS!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

            else:
                get_value = event.pos[0]
                col = math.floor(event.pos[0])//PXLSIZE

                if column_available(board, col):
                    row = get_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if connect_four(board, 2):
                        label = game_over_message.render("PLAYER 2 WINS!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            draw_board(screen, board)
            pygame.display.update()

            if(game_over):
                pygame.time.delay(5000)

            turn += 1
            turn = turn % 2
