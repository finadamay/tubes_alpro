from kivymd.app import MDApp
from kivymd.uix.screenmanager import screenmanager
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.size = (420, 580)

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class LapakNgoding(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            Hallog(name="hallog")
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
if __name__ == '__main__':
    LabelBase.register(name="Atma")
    LabelBase.register(name="Tagline")
    LabelBase.register(name="Line")
    LapakNgoding().run()