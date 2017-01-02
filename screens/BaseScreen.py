
import pygame
import json
from constants import *
from polygon_tools import *

class BaseScreen:

    def __init__(self, main_callback, name):
        self.main_callback = main_callback
        self.background = pygame.image.load("screens/" + name + ".png")
        with open("screens/" + name +  ".json", 'r') as fd:
            self.data = json.load(fd)


    def update(self, event):
        if event.type == LMB_RELEASE:
            self.handleClickEvent(event.pos)


    def draw(self, surface):
        surface.blit(self.background, (0, 0))


        self.drawScreen(surface)
        self.drawDebug(surface)


    def handleClickEvent(self, pos):
        for button in self.data['buttons']:
            areapoints = button['clickarea']
            aabb = getAABB(areapoints)
            if aabb.collidepoint(pos) and point_inside_polygon(pos[0], pos[1], areapoints):
                self.buttonClicked(button)

    def buttonClicked(self, button):
        raise Exception("Needs to to be implemented in subclass")

    def drawScreen(self, surface):
        #Override if needed
        pass

    def set_data(self, data):
        #Override if you want to get data passed into your screen
        pass

    def update_model(self):
        #Called before a screen ist shown
        pass

    def drawDebug(self,surface):
        if DEBUG:
            for btn in self.data['buttons']:
                pygame.draw.polygon(surface, BLUE, btn['clickarea'], 2)

                if DEBUG:
                    aabb = getAABB(btn['clickarea'])
                    pygame.draw.rect(surface, RED, aabb, 2)