from kivy.properties import DictProperty

class ThemeManager:
    current_theme = "dark"  #Default theme is dark

    themes = {
        "home": {
            "background": (0.5, 0.5, 0.5, 1),  # Always Grey
            "text": (1, 1, 1, 1),  # White Text
            "button_encrypt_light": (0.2, 0.4, 1, 1),  #Lighter Blue in Light Mode
            "button_encrypt_dark": (0.0, 0.0, 0.6, 1),  #Darker Blue in Dark Mode
            "button_decrypt_light": (1, 0.4, 0.4, 1),  #Lighter Red in Light Mode
            "button_decrypt_dark": (0.6, 0.0, 0.0, 1),  #Darker Red in Dark Mode
            "button_text": (1, 1, 1, 1),  # White Text
        },
        "encrypt_light": {
            "background": (1, 1, 1, 1),  #White
            "text": (0, 0, 0, 1),  #Black
            "button": (0.4, 0.6, 1, 1),  #Light Blue
            "button_text": (1, 1, 1, 1),  #White
        },
        "encrypt_dark": {
            "background": (0.05, 0.05, 0.1, 1),  #Dark Blue
            "text": (0.8, 0.9, 1, 1),  #Cyan
            "button": (0.1, 0.3, 0.6, 1),  #Dark Blue
            "button_text": (1, 1, 1, 1),  #White
        },
        "decrypt_light": {
            "background": (0.7, 0.7, 0.7, 1),  #Light Grey Background
            "text": (0, 0, 0, 1),  #Black
            "button": (1, 0.4, 0.4, 1),  #Light Red
            "button_text": (1, 1, 1, 1),  #White
        },
        "decrypt_dark": {
            "background": (0.3, 0.3, 0.3, 1),  #Dark Grey Background
            "text": (1, 1, 1, 1),  #White
            "button": (0.6, 0.1, 0.1, 1),  #Dark Red
            "button_text": (1, 1, 1, 1),  #White
        },
    }

    @classmethod
    def toggle_theme(cls):
        """Switch between light and dark mode globally."""
        cls.current_theme = "dark" if cls.current_theme == "light" else "light"

    @classmethod
    def get_theme(cls, screen_name):
        """Returns the theme settings based on the screen."""
        if screen_name == "home":
            return cls.themes["home"]
        elif screen_name == "encrypt":
            return cls.themes["encrypt_dark"] if cls.current_theme == "dark" else cls.themes["encrypt_light"]
        elif screen_name == "decrypt":
            return cls.themes["decrypt_dark"] if cls.current_theme == "dark" else cls.themes["decrypt_light"]
