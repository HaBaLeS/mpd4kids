from constants import *
from screens.BaseScreen import BaseScreen

class PlayControll(BaseScreen):


    def __init__(self, main_callback):
        super().__init__(main_callback, "play_controll")


    def buttonClicked(self, button):
        btn_funct = button['function']

        print(btn_funct)

        if "back" == btn_funct:
            self.main_callback.switch_to_screen("album_select")