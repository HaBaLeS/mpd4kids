from constants import *
from screens.BaseScreen import BaseScreen
from render_utils import render_textrect


class AbSelectScreen(BaseScreen):


    def __init__(self,main_callback):
        super().__init__(main_callback, "ab_select")
        self.model = {}
        self.model['artist'] = main_callback.mpd_player.getAudioBookArtists()
        self.model['offset'] = 0

        self.update_model()


    def buttonClicked(self, button):
        btn_funct = button['function']

        selected_artist = None

        if "next" == btn_funct:
            if self.model['offset']+4 <= len(self.model['artist']):
                self.model['offset'] =  self.model['offset']+4
                self.update_model()

        elif "prev" == btn_funct:
            if self.model['offset'] > 0:
                self.model['offset'] = self.model['offset'] - 4
                self.update_model()

        elif "back" == btn_funct:
            self.main_callback.switch_to_screen("start")


        elif "select_0" == btn_funct:
            if len(self.model['page_artist']) >0:
                selected_artist = self.model['page_artist'][0]
        elif "select_1" == btn_funct:
            if len(self.model['page_artist']) > 1:
                selected_artist = self.model['page_artist'][1]
        elif "select_2" == btn_funct:
            if len(self.model['page_artist']) > 2:
                selected_artist = self.model['page_artist'][2]
        elif "select_3" == btn_funct:
            if len(self.model['page_artist']) > 3:
                selected_artist = self.model['page_artist'][3]

        else:
            print(btn_funct)

        if selected_artist is not None:
            self.main_callback.switch_to_screen("album_select", selected_artist)


    def drawScreen(self, surface):

        if len(self.images) > 0:
            surface.blit(self.images[0], (150, 30))
        if len(self.images) > 1:
            surface.blit(self.images[1], (450, 30))
        if len(self.images) > 2:
            surface.blit(self.images[2], (150, 270))
        if len(self.images) > 3:
            surface.blit(self.images[3], (450, 270))

    def update_model(self):

        start_idx = self.model['offset']
        end_idx = start_idx +4;

        if end_idx > len(self.model['artist']):
            end_idx = end_idx -( end_idx - len(self.model['artist']))

        print(str(start_idx) + " : " + str(end_idx))
        page_artist = self.model['artist'][start_idx:end_idx]

        self.model["page_artist"] = page_artist

        os_font = pygame.font.Font("font/OpenSans-Regular.ttf", 18)
        os_font.set_bold(True)

        self.images = []
        for i in range(0,len(page_artist)):
            self.images.append(pygame.Surface((200,200)))
            self.images[i].fill(BLUE)

            artist = page_artist[i]
            tw = os_font.size(artist)
            print(tw)

            text_surface = render_textrect(artist, os_font,self.images[i],WHITE,None, 1)
            text_bounds = text_surface.get_rect()
            self.images[i].blit(text_surface, text_bounds)

            self.images[i].convert()


