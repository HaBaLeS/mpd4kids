from pygame.event import Event

from pygame.locals import *
from pygame import time
from screens import start
from constants import *



def startFirst():

    pygame.init()



    DISPLAYSURF = pygame.display.set_mode((800, 480), pygame.NOFRAME)
    print(pygame.display.Info())

    #currentscreen = first.FirstScreen()
    currentscreen = start.StartScreen()

    running = True
    clicked = False

    while running:  # main game loop
        for evt in pygame.event.get():
            if evt.type == KEYDOWN and evt.key == K_ESCAPE:
                running = False

            l,m,r = pygame.mouse.get_pressed()
            if clicked and l == 0:
                clicked = False
                pygame.event.post(Event(LMB_RELEASE,{'pos' : pygame.mouse.get_pos()}))
                print("release")
            if l == 1:
                clicked = True

            currentscreen.update(evt)

        currentscreen.draw(DISPLAYSURF)
        pygame.display.update()

        # do your non-rendering game loop computation here
        # to reduce CPU usage, call this guy:
        time.wait(20)


if __name__ == "__main__":
    startFirst()

