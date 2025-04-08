from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from Utils.theme import ThemeManager
from Utils.utils import get_message_bits, get_image, get_message_length, is_even, to_binary, to_char
import cv2


# Corrected KV file paths (relative to Frontend folder)
Builder.load_file("Looks/home.kv")
Builder.load_file("Looks/encrypt.kv")
Builder.load_file("Looks/decrypt.kv")

class HomeScreen(Screen):
    def toggle_theme(self):
        app = App.get_running_app()
        app.toggle_theme()

class MyApp(App):
    theme_mode = BooleanProperty(False)  # False = Dark Mode, True = Light Mode
    reused_pattern = None
    reused_code = None

    def build(self):
        from Screens.encrypt import EncryptScreen
        from Screens.decrypt import DecryptScreen

        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(EncryptScreen(name="encrypt"))
        self.sm.add_widget(DecryptScreen(name="decrypt"))

        self.update_theme()
        return self.sm

    def toggle_theme(self):
        ThemeManager.toggle_theme()
        self.update_theme()

    def update_theme(self):
        for screen in self.sm.screens:
            theme = ThemeManager.get_theme(screen.name)

            # Update background color
            if hasattr(screen, "canvas") and screen.canvas.before.children:
                for instruction in screen.canvas.before.children:
                    if hasattr(instruction, "rgba"):
                        instruction.rgba = theme["background"]

            # Update text and button colors
            for widget in screen.walk():
                if hasattr(widget, "color"):
                    widget.color = theme["text"]

                if isinstance(widget, Button):
                    if screen.name == "home":
                        if "encrypt" in widget.text.lower():
                            widget.background_color = ThemeManager.themes["home"]["button_encrypt"][ThemeManager.current_theme]
                        elif "decrypt" in widget.text.lower():
                            widget.background_color = ThemeManager.themes["home"]["button_decrypt"][ThemeManager.current_theme]
                    else:
                        widget.background_color = theme["button"]
                    widget.color = theme["button_text"]

if __name__ == '__main__':
    MyApp().run()
