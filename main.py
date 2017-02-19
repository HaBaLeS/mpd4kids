from pygame.event import Event

from audio_subsystem import AudioControll
from audio_subsystem import AudioCollection
from audio_subsystem.mpd_utils import MPDAudioSubsystem

from constants import *
from pygame import time
from pygame.locals import *
from screens import ab_select
from screens import album_select
from screens import play_controll
from screens import start



class Main():

    def __init__(self):

        pygame.init()
        self.init_audio_subsystem()

        DISPLAYSURF = pygame.display.set_mode((800, 480), pygame.NOFRAME)
        print(pygame.display.Info())


        self.screens = {
            "start": start.StartScreen(self),
            "ab_select": ab_select.AbSelectScreen(self),
            "album_select" : album_select.AlbumSelectScreen(self),
            "play_controll": play_controll.PlayControll(self)
        }

        self.currentscreen = self.screens['start']
        self.currentscreen.update_model()

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

    def switch_to_screen(self, screen_name, data = None):
        self.currentscreen = self.screens[screen_name]
        if data :
            self.currentscreen.set_data(data)
        self.currentscreen.update_model()

    def init_audio_subsystem(self):

        #Initialize which implementation of the Library Management and Player Controll should be loaded.
        # This can ba anything from flat file, mpd, dnla or whatever you want to build.
        # Even spotyfy and Google/Amazon Music should be possible as long as connectors exist
        self.audio_controll = MPDAudioSubsystem()
        self.audio_collection = self.audio_controll


if __name__ == "__main__":
    Main()

