from kivymd.app import MDApp
from kivy.uix.screen import MdScreen
from kivy.lang import Builder

class Hallog(MdScreen):
    def __init__(self, **kw):
        Builder.load.file("kv/uas.kv")
        super().__init__(**kw)