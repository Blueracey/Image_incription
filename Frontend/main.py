from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from Utils.utils import get_message_bits, get_image, get_message_length, is_even, to_binary, to_char
import kivy.resources
import cv2
import sys
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

#Fix for PyInstaller packaged paths
if hasattr(sys, '_MEIPASS'):
    resource_path = sys._MEIPASS
else:
    resource_path = os.path.abspath(".")

# Load KV files using absolute paths
Builder.load_file(os.path.join(resource_path, "Looks", "home.kv"))
Builder.load_file(os.path.join(resource_path, "Looks", "encrypt.kv"))
Builder.load_file(os.path.join(resource_path, "Looks", "decrypt.kv"))

#Add resource path if running from PyInstaller .exe
if getattr(sys, 'frozen', False):
    kivy.resources.resource_add_path(sys._MEIPASS)

class HomeScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        from Screens.encrypt import EncryptScreen
        from Screens.decrypt import DecryptScreen

        self.reused_pattern = None
        self.reused_code = None

        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(EncryptScreen(name="encrypt"))
        self.sm.add_widget(DecryptScreen(name="decrypt"))

        return self.sm

if __name__ == '__main__':
    MyApp().run()