import pygame
from button import Button
from grid import Grid
from game import TicTacToe,Move
import time


def redrawWindow3(screen,button1,button2):
    screen.fill((255,255,255))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GeeksForGeeks', True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (350,100) 
    screen.blit(text, textRect) 
    button1.draw(screen,(0,0,255))
    button2.draw(screen,(0,0,255))
    pygame.display.flip()

def gameoverscreen(screen,val):
    screen.fill((255,255,255))
    running=True
    greenButton = Button((255,255,255),150,125,500,70,'Play again')
    button2 = Button((255,255,255),150,235,500,70,'Quit')
    while running:
        redrawWindow3(screen,greenButton,button2)
        pygame.display.update()

        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()

            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                quit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if greenButton.isOver(pos):
                    dropdown(screen)
                    print(greenButton.text)
                elif button2.isOver(pos):
                    running=False
                    pygame.quit()
                    print(button2.text)
                
            if event.type==pygame.MOUSEMOTION:
                if greenButton.isOver(pos):
                    greenButton.color=(0,0,255)
                else:
                    greenButton.color=(255,255,255)

                if button2.isOver(pos):
                    button2.color=(0,0,255)
                else:
                    button2.color=(255,255,255)

            

def show_board(screen):

    # screen.fill((255,255,255))
    grid=Grid()
    ticgame=TicTacToe()
    running=True
    while running:
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            position=[]
            if event.type==pygame.QUIT:
                running=False

            elif event.type==pygame.MOUSEBUTTONDOWN:
                if pos[0]<=220 and pos[1]<=220:
                    position=[0,0]        
                elif pos[0]>220 and pos[0]<=440 and pos[1]<=220:
                    position=[0,1]  
                elif pos[0]>440 and pos[0]<=700 and pos[1]<=220:
                    position=[0,2]
                elif pos[0]<=200 and pos[1]<=440:
                    position=[1,0]
                elif pos[0]>220 and pos[0]<=440 and pos[1]<=440:
                    position=[1,1]
                elif pos[0]>440 and pos[0]<=700 and pos[1]<=440:
                    position=[1,2]
                elif pos[0]<=220 and pos[1]>440:
                    position=[2,0]
                elif pos[0]>220 and pos[0]<=440 and pos[1]>440:
                    position=[2,1]
                elif pos[0]>440 and pos[0]<=700 and pos[1]>440:
                    position=[2,2]

                font=pygame.font.Font(None,700//18)
                text=font.render('X',True,(255,0,0))
                screen.blit(text,pos)
                pygame.display.update()

                comp_mov=Move(-1,-1)
                print(position)
                ticgame.board[position[0]][position[1]]='x'
                score=ticgame.utility()
                if score==1 or score==-1 or (score==0 and ticgame.movesLeft==False):
                    gameoverscreen(screen,score)
                    break
                ticgame.board[position[0]][position[1]]='_'
                comp_mov=ticgame.game_move(position)   

                if comp_mov.x==0 and comp_mov.y==0:
                    pos2=[110,110]
                elif comp_mov.x==0 and comp_mov.y==1:
                    pos2=[330,110]
                elif comp_mov.x==0 and comp_mov.y==2:
                    pos2=[620,110]
                elif comp_mov.x==1 and comp_mov.y==0:
                    pos2=[110,330]
                elif comp_mov.x==1 and comp_mov.y==1:
                    pos2=[330,330]
                elif comp_mov.x==1 and comp_mov.y==2:
                    pos2=[620,330]
                elif comp_mov.x==2 and comp_mov.y==0:
                    pos2=[110,620]
                elif comp_mov.x==2 and comp_mov.y==1:
                    pos2=[330,620]
                elif comp_mov.x==2 and comp_mov.y==2:
                    pos2=[620,620]

                font = pygame.font.Font(None,700//18) 
                text = font.render('O', True, (0,0,0))
                screen.blit(text,pos2)
                pygame.display.update()

                score=ticgame.utility()
                if score==1 or score==-1 or (score==0 and ticgame.movesLeft==False):
                    gameoverscreen(screen,score)
                    break



        screen.fill((255,255,255))
        grid.draw(screen)
        pygame.display.flip()



    
    


def Minimax(screen):
    show_board(screen)


def redrawWindow2(screen,button1,button2,button3,button4):
    screen.fill((255,255,255))
    button1.draw(screen,(0,0,255))
    button2.draw(screen,(0,0,255))
    button3.draw(screen,(0,0,255))
    button4.draw(screen,(0,0,255))
    pygame.display.flip()

def dropdown(screen):
    screen.fill((255,255,255))
    run=True
    greenButton = Button((255,255,255),150,125,500,70,'Play against Minimax')
    button2 = Button((255,255,255),150,235,500,70,'Play against Minimax with alpha beta pruning')
    button3 = Button((255,255,255),150,345,500,70,'Play against Depth Limited Minimax with heuristic')
    button4 = Button((255,255,255),150,455,500,70,'Play against Depth Limited Minimax with alpha beta pruning')
    while run:
        redrawWindow2(screen,greenButton,button2,button3,button4)
        pygame.display.update()

        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()

            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                quit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if greenButton.isOver(pos):
                    Minimax(screen)
                    print(greenButton.text)
                elif button2.isOver(pos):
                    print(button2.text)
                elif button3.isOver(pos):
                    print(button3.text)
                elif button4.isOver(pos):
                    print(button4.text)

            if event.type==pygame.MOUSEMOTION:
                if greenButton.isOver(pos):
                    greenButton.color=(0,0,255)
                else:
                    greenButton.color=(255,255,255)

                if button2.isOver(pos):
                    button2.color=(0,0,255)
                else:
                    button2.color=(255,255,255)

                if button3.isOver(pos):
                    button3.color=(0,0,255)
                else:
                    button3.color=(255,255,255)

                if button4.isOver(pos):
                    button4.color=(0,0,255)
                else:
                    button4.color=(255,255,255)




def redrawWindow(button,button2):
    screen.fill((255,255,255))
    button.draw(screen,(0,0,255))
    button2.draw(screen,(0,0,255))

pygame.init()
screen=pygame.display.set_mode((700,700))
screen.fill((255,255,255))



run=True
greenButton = Button((255,255,255),150,125,175,70,'Tic Tac Toe',40)
button2 = Button((255,255,255),150,235,175,70,'OFT',40)
while run:
    redrawWindow(greenButton,button2)
    pygame.display.update()

    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()

        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
                dropdown(screen)
            elif button2.isOver(pos):
                dropdown(screen)

        if event.type==pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color=(0,0,255)
            else:
                greenButton.color=(255,255,255)

            if button2.isOver(pos):
                button2.color=(0,0,255)
            else:
                button2.color=(255,255,255)

