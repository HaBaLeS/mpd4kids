import pygame, sys
from pygame.locals import *
from pygame import time
import json

BLACK = (0, 0, 0)

def draw_click_areas(DISPLAYSURF, area_point_list):

    for area in area_point_list:
        if len(area) > 1:
            pygame.draw.polygon(DISPLAYSURF, BLACK,area, 4)


def dumpAreas(area_point_lists, name):
    data = {}
    data['screen_name'] = name
    data['buttons'] = []

    for area in area_point_lists:
        if len(area) > 1:
            ad = {}
            ad['name'] = ""
            ad['function'] = ""
            ad['clickarea'] = area
            data['buttons'].append(ad)

    jd = json.dumps(data, sort_keys=True,indent = 4, separators = (',', ': '))
    with open("../screens/"+ data['screen_name'] + ".json", 'w') as fd:
        fd.write(jd)

    print(jd)

def startFirst(name):

    pygame.init()

    running = True

    DISPLAYSURF = pygame.display.set_mode((800, 480), pygame.NOFRAME)
    print(pygame.display.Info())

    background = pygame.image.load("../screens/"+name+".png")
    os_font = pygame.font.Font("../font/OpenSans-Regular.ttf",12)

    text_surface = os_font.render("Blafasel",True, BLACK)
    text_bounds = text_surface.get_rect()
    text_bounds.center = (100,100)

    area_point_lists = []
    curr_list = []

    area_point_lists.append(curr_list)

    while running:  # main game loop
        for evt in pygame.event.get():
            #print(evt)
            if evt.type == KEYDOWN and evt.key == K_ESCAPE:
                running = False

            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    print("add to list")
                    curr_list.append(evt.pos)
                if evt.button == 3:
                    print("finish object")
                    curr_list = []
                    area_point_lists.append(curr_list)




        DISPLAYSURF.blit(background, (0, 0))

        draw_click_areas(DISPLAYSURF, area_point_lists)

        DISPLAYSURF.blit(text_surface, text_bounds)

        pygame.display.update()

        # do your non-rendering game loop computation here
        # to reduce CPU usage, call this guy:
        time.wait(20)

    dumpAreas(area_point_lists,name)

if __name__ == "__main__":
    startFirst("start")

