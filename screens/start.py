from constants import *
from screens.BaseScreen import BaseScreen


class StartScreen(BaseScreen):

    def __init__(self,main_callback):
        super().__init__(main_callback, "start")


    def buttonClicked(self, button):
        btn_funct = button['function']

        print(btn_funct)

        if "exit_player" == btn_funct:
            self.main_callback.exit_player()

        elif "hoerbuch" == btn_funct:
            self.main_callback.switch_to_screen("ab_select")


