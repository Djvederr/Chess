import numpy as np
import pygame
import sys

pygame.init()
size=100
gap=10
w_size=size*3+gap*4
screen=pygame.display.set_mode([w_size,w_size+50])
screen.fill((0,0,255))
font1 = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 25)

def display_board (board):
    y=gap
    for row in range(3):
        x=gap
        for col in range(3):          
            pygame.draw.rect(screen,(255,0,0),(x,y,size,size))
            if board[row][col]==1:
                text = font1.render('O', True, (0,0,255))
            elif board[row][col]==2:
                text = font1.render('X', True, (0,0,255))
            else:
                text = font1.render(' ', True, (0,0,255))
            screen.blit(text, (x+20, y+20))     
            x=x+size+gap
        y=y+size+gap
    pygame.display.flip()
    
def message(m):
    pygame.draw.rect(screen,(0,0,0),(0,w_size,w_size,50))
    pygame.display.flip()
    text2 = font2.render('Status:'+m, True, (255,255,255))
    screen.blit(text2, (5, w_size+5))     
    pygame.display.flip()

def drop_pc(pc, row, col, board):
    if board[row][col] == 0:
        board[row][col] = pc
        return True
    else:
        return False
    


def winning_move(pc):#,row,col,board):

    # check rows
    for r in range(3):
        if board[r][0]==board[r][1]==board[r][2]==pc:
            return True
   # check cols
    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]==pc:
            return True
   # check +ve diagonal
    if board[0][0]==board[1][1]==board[2][2]==pc:
            return True
   # check -ve diagonal
    if board[0][2]==board[1][1]==board[2][0]==pc:
            return True


    
def get_cellClicked(xpos,ypos):
   
    row=ypos//size
    col=xpos//size
    return (row,col)

    
board = np.zeros((3,3))
game_over=False
turn = 0
display_board(board)
message("Player 1 Move")
pygame.display.flip()


while True:
    if turn==9 and not game_over:
        message("It's a Tie")
        game_over =True
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            game_over=True
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            cell = get_cellClicked(event.pos[0],event.pos[1])
                       
            
            if turn%2 == 0:
               
                if drop_pc(1, cell[0], cell[1], board):
                    turn = turn + 1
                    if winning_move(1):#,row,col,board):
                        message("Player 1 Wins")
                        print("Player 1 Wins")
                        game_over =True
                    else:
                        message("Player 2 Move")
                else:
                    message("Choose an Empty Box")
                
                    
                               
            else:
                if drop_pc(2, cell[0], cell[1], board):
                    turn = turn + 1
                    if winning_move(2):#,row,col,board):
                        message("Player 2 Wins")
                        print("Player 2 Wins")
                        game_over =True
                    else:
                        message("Player 1 Move")
                else:
                    message("Choose an Empty Box")
                
            display_board(board)
            pygame.display.flip()
            


