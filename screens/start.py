
import pygame
from pygame.locals import *
import json
from constants import *
from polygon_tools import *




class StartScreen:


    def __init__(self):
        self.background = pygame.image.load("screens/start.png")
        with open("screens/start.json",'r') as fd:
            self.data = json.load(fd)

    def update(self, event):
        #if event.type == MOUSEBUTTONUP  and event.button == 1:
         #   print("click")
        if event.type == LMB_RELEASE:
            self.handleClickEvent(event.pos)
        pass

    def draw(self, surface):
        surface.blit(self.background, (0,0))
        if DEBUG:
            for btn in self.data['buttons']:
                pygame.draw.polygon(surface, BLUE, btn['clickarea'], 2)


                if DEBUG:
                    aabb = getAABB(btn['clickarea'])
                    pygame.draw.rect(surface, RED, aabb, 2)



    def handleClickEvent(self,pos):
        for button in self.data['buttons']:
            areapoints = button['clickarea']
            aabb = getAABB(areapoints)
            if aabb.collidepoint(pos) and point_inside_polygon(pos[0],pos[1], areapoints):
                print("MAAAATCH")
        pass


