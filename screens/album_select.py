from constants import *
from screens.BaseScreen import BaseScreen
from render_utils import render_textrect
from mutagen import File

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

        selected_album = None

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

        elif "album_0" == btn_funct:
            if len(self.model['page_album']) >0:
                selected_album = self.model['page_album'][0]
        elif "album_1" == btn_funct:
            if len(self.model['page_album']) > 1:
                selected_album = self.model['page_album'][1]
        elif "album_2" == btn_funct:
            if len(self.model['page_album']) > 2:
                selected_album = self.model['page_album'][2]
        elif "album_3" == btn_funct:
            if len(self.model['page_album']) > 3:
                selected_album = self.model['page_album'][3]

        if selected_album:
            self.main_callback.switch_to_screen("play_controll", selected_album)
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
            album = page_album[i]
            self.images.append(pygame.Surface((200,200)))
            self.images[i].fill(BLUE)

            track = self.main_callback.mpd_player.get_first_track_of_album(album)
            file = File(CONFIG_mpd_library_path + track['file'])  # mutagen can automatically detect format and type of tags

            if "APIC:" in file.tags.keys():
                artwork = file.tags['APIC:'].data  # access APIC frame and grab the image
                with open('tmp_album_cover.jpg', 'wb') as img:
                    img.write(artwork)  # write artwork to new image
                album_cover = pygame.image.load("tmp_album_cover.jpg")
                foo = pygame.transform.scale(album_cover, (200, 200))
                self.images[i].blit(foo, (0, 0))

            else:
                text_surface = render_textrect(album, os_font, self.images[i], WHITE, None, 1)
                text_bounds = text_surface.get_rect()
                self.images[i].blit(text_surface, text_bounds)

            self.images[i].convert()


    def set_data(self, artist):
        self.model['selected_artist'] = artist
        self.model['offset'] = 0


