from pygame.event import Event

from pygame.locals import *
from pygame import time
from screens import start
from screens import ab_select

from constants import *



class Main():

    def __init__(self):

        pygame.init()

        DISPLAYSURF = pygame.display.set_mode((800, 480), pygame.NOFRAME)
        print(pygame.display.Info())


        self.screens = {
            "start": start.StartScreen(self),
            "ab_select": ab_select.AbSelectScreen(self)
        }

        self.currentscreen = self.screens['start']

        self.running = True
        clicked = False

        while self.running:  # main game loop
            for evt in pygame.event.get():
                if evt.type == KEYDOWN and evt.key == K_ESCAPE:
                    self.running = False

                l,m,r = pygame.mouse.get_pressed()
                if clicked and l == 0:
                    clicked = False
                    pygame.event.post(Event(LMB_RELEASE,{'pos' : pygame.mouse.get_pos()}))
                if l == 1:
                    clicked = True

                self.currentscreen.update(evt)

            self.currentscreen.draw(DISPLAYSURF)
            pygame.display.update()

            # do your non-rendering game loop computation here
            # to reduce CPU usage, call this guy:
            time.wait(20)

    def exit_player(self):
        self.running = False

    def switch_to_screen(self, screen_name):
        self.currentscreen = self.screens[screen_name]



if __name__ == "__main__":
    Main()

