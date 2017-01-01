from constants import *
from screens.BaseScreen import BaseScreen


class AbSelectScreen(BaseScreen):

    def __init__(self,main_callback):
        super().__init__(main_callback, "ab_select")


    def buttonClicked(self, button):
        btn_funct = button['function']

        print(btn_funct)




