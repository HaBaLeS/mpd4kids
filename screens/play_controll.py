from constants import *
from screens.BaseScreen import BaseScreen
from render_utils import render_textrect

class PlayControll(BaseScreen):




    def __init__(self, main_callback):
        super().__init__(main_callback, "play_controll")
        self.model = {
            "selected_album": None,
        }
        if main_callback.audio_controll.currentsong():
            self.model['selected_album'] = main_callback.audio_controll.currentsong()['album']

        self.cover = pygame.Surface(cover_size)
        self.os_font = pygame.font.Font("font/OpenSans-Regular.ttf", 18)
        self.os_font.set_bold(True)


    def buttonClicked(self, button):
        btn_funct = button['function']

        if "back" == btn_funct:
            self.main_callback.switch_to_screen("album_select")

        if "play_pause" == btn_funct:
            self.main_callback.audio_controll.play_pause()

        if "next" == btn_funct:
            status = self.main_callback.audio_controll.playback_status()
            if "nextsong" in status:
                self.main_callback.audio_controll.next()

        if "prev" == btn_funct:
            self.main_callback.audio_controll.prev()

        self.update_model()

    def set_data(self, album):
        if album and not self.model['selected_album'] == album:
            self.main_callback.audio_controll.stop()
            self.main_callback.audio_controll.clear_list_and_load_album(album)
            self.main_callback.audio_controll.start()

            self.main_callback.audio_controll.playback_status()
            print(self.main_callback.audio_controll.currentsong())

        self.model['selected_album'] = album
        self.model['offset'] = 0

    def update_model(self):
        self.cover = pygame.Surface(cover_size)
        album =  self.model['selected_album']

        album_cover = self.main_callback.audio_controll.get_album_coverart(album,cover_size)
        if album_cover:
            self.cover.blit(album_cover, (0, 0))
        else:
            text_surface = render_textrect(album, self.os_font, self.cover, WHITE, None, 1)
            text_bounds = text_surface.get_rect()
            self.cover.blit(text_surface, text_bounds)

        self.cover.convert()

        current = self.main_callback.audio_controll.currentsong()
        status = self.main_callback.audio_controll.playback_status()

        if current and status:
            track_count = str(int(current['pos']) + 1) + "/" + str(status['playlistlength'])
            self.title_surface = self.os_font.render(track_count + " " + current['title'], True, WHITE)



    def drawScreen(self, surface):
        surface.blit(self.cover, (20,20))
        surface.blit(self.title_surface, (450,250))

