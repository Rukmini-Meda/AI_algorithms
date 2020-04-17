import pygame

class Grid:
    def __init__(self):
        self.grid_lines=[((0,220),(700,220)),((0,440),(700,440)),((220,0),(220,700)),((440,0),(440,700))]

    def draw(self,surface):
        for line in self.grid_lines:
            pygame.draw.line(surface,(0,0,0),line[0],line[1],2)