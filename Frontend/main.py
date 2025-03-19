from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from Utils.theme import ThemeManager

#Load KV files
Builder.load_file("Looks/home.kv")
Builder.load_file("Looks/encrypt.kv")
Builder.load_file("Looks/decrypt.kv")

class HomeScreen(Screen):
    def toggle_theme(self):
        """Toggle the global theme mode."""
        app = App.get_running_app()
        app.toggle_theme()

class MyApp(App):
    theme_mode = BooleanProperty(False)  #False = Dark Mode, True = Light Mode

    def build(self):
        from Screens.encrypt import EncryptScreen 
        from Screens.decrypt import DecryptScreen

        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(EncryptScreen(name="encrypt"))
        self.sm.add_widget(DecryptScreen(name="decrypt"))
        return self.sm

    def toggle_theme(self):
        """Toggle between light and dark mode globally."""
        ThemeManager.toggle_theme()
        self.update_theme()

    def update_theme(self):
        """Apply theme updates to all screens."""
        for screen in self.sm.screens:
            theme = ThemeManager.get_theme(screen.name)

            if hasattr(screen, "canvas") and screen.canvas.before.children:
                for instruction in screen.canvas.before.children:
                    if hasattr(instruction, "rgba"):
                        instruction.rgba = theme["background"]

            #Update text and button colors
            for widget in screen.walk():
                if hasattr(widget, "color"):
                    widget.color = theme["text"]
                if isinstance(widget, Button):
                    if screen.name == "home":
                        if "Encrypt" in widget.text:
                            widget.background_color = theme["button_encrypt_dark"] if ThemeManager.current_theme == "dark" else theme["button_encrypt_light"]
                        elif "Decrypt" in widget.text:
                            widget.background_color = theme["button_decrypt_dark"] if ThemeManager.current_theme == "dark" else theme["button_decrypt_light"]
                    else:
                        widget.background_color = theme["button"]
                    widget.color = theme["button_text"]

if __name__ == '__main__':
    MyApp().run()
