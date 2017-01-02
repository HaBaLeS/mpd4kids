from constants import *
from screens.BaseScreen import BaseScreen


class AlbumSelectScreen(BaseScreen):


    def __init__(self,main_callback):
        super().__init__(main_callback, "album_select")
        self.model = {}
        self.model['selected_artist'] = ""
        self.model['albums'] = []
        self.model['offset'] = 0

        self.update_model()


    def buttonClicked(self, button):
        btn_funct = button['function']

        if "next" == btn_funct:
            if self.model['offset']+4 <= len(self.model['albums']):
                self.model['offset'] =  self.model['offset']+4
                self.update_model()

        elif "prev" == btn_funct:
            if self.model['offset'] > 0:
                self.model['offset'] = self.model['offset'] - 4
                self.update_model()

        elif "back" == btn_funct:
            self.main_callback.switch_to_screen("ab_select")

        elif "select_0" == btn_funct:
            if len(self.model['page_artist']) >0:
                artist = self.model['page_artist'][0]
                print(artist)
        elif "select_1" == btn_funct:
            if len(self.model['page_artist']) > 1:
                artist = self.model['page_artist'][1]
                print(artist)
        elif "select_2" == btn_funct:
            if len(self.model['page_artist']) > 2:
                artist = self.model['page_artist'][2]
                print(artist)
        elif "select_3" == btn_funct:
            if len(self.model['page_artist']) > 3:
                artist = self.model['page_artist'][3]
                print(artist)

        print(btn_funct)


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

        self.model['albums'] = self.main_callback.mpd_player.get_album_for_artist(self.model['selected_artist'])

        start_idx = self.model['offset']
        end_idx = start_idx +4;

        if end_idx > len(self.model['albums']):
            end_idx = end_idx -( end_idx - len(self.model['albums']))

        print(str(start_idx) + " : " + str(end_idx))
        page_album = self.model['albums'][start_idx:end_idx]

        self.model["page_album"] = page_album

        os_font = pygame.font.Font("font/OpenSans-Regular.ttf", 18)
        os_font.set_bold(True)

        self.images = []
        for i in range(0,len(page_album)):
            self.images.append(pygame.Surface((200,200)))
            self.images[i].fill(BLUE)

            album = page_album[i]
            tw = os_font.size(album)
            print(tw)
            text_surface = os_font.render(album, True, WHITE)
            text_bounds = text_surface.get_rect()
            text_bounds.center = (100, 150)
            self.images[i].blit(text_surface, text_bounds)

            self.images[i].convert()


    def set_data(self, artist):
        self.model['selected_artist'] = artist


