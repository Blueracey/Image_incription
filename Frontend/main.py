from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from Utils.utils import get_message_bits, get_image, get_message_length, is_even, to_binary, to_char
import cv2

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Load KV files
Builder.load_file("Looks/home.kv")
Builder.load_file("Looks/encrypt.kv")
Builder.load_file("Looks/decrypt.kv")

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