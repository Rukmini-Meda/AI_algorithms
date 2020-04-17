import pygame
from button import Button
from mainscreen import dropdown

def redrawWindow(screen,button1,button2,val):
    screen.fill((255,255,255))
    font = pygame.font.Font('freesansbold.ttf', 32) 
    if val==1:
        string="You have lost. Better luck next time!!"
    elif val==-1:
        string="Congratulations, you have won!!"
    else:
        string="Its a DRAW!!"
    text = font.render(string, True, (0,0,0))
    pygame.display.update()
    button1.draw(screen,(0,0,255))
    button2.draw(screen,(0,0,255))
    pygame.display.flip()

def gameoverscreen(screen,val):
    screen.fill((255,255,255))
    running=True
    greenButton = Button((255,255,255),150,125,500,70,'Play again')
    button2 = Button((255,255,255),150,235,500,70,'Quit')
    while running:
        redrawWindow(screen,greenButton,button2,val)
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

                