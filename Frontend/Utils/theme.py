class ThemeManager:
    current_theme = "dark"  # Start in dark mode

    themes = {
        "home": {
            "background": (0.1, 0.1, 0.1, 1),
            "text": (1, 1, 1, 1),
            "button_text": (1, 1, 1, 1),
            "button_encrypt": {
                "dark": (0.2, 0.4, 0.9, 1),   # Bright Blue
                "light": (0.5, 0.7, 1, 1),    # Light Blue
            },
            "button_decrypt": {
                "dark": (0.9, 0.4, 0.1, 1),   # Bright Orange
                "light": (1, 0.5, 0.2, 1),    # Light Orange
            }
        },
        "encrypt_dark": {
            "background": (0.05, 0.05, 0.1, 1),
            "text": (1, 1, 1, 1),
            "button": (0.2, 0.4, 0.9, 1),
            "button_text": (1, 1, 1, 1),
        },
        "encrypt_light": {
            "background": (1, 1, 1, 1),
            "text": (0, 0, 0, 1),
            "button": (0.5, 0.7, 1, 1),
            "button_text": (0, 0, 0, 1),
        },
        "decrypt_dark": {
            "background": (0.3, 0.3, 0.3, 1),
            "text": (1, 1, 1, 1),
            "button": (0.9, 0.4, 0.1, 1),
            "button_text": (1, 1, 1, 1),
        },
        "decrypt_light": {
            "background": (0.85, 0.85, 0.85, 1),
            "text": (0, 0, 0, 1),
            "button": (1, 0.5, 0.2, 1),
            "button_text": (0, 0, 0, 1),
        }
    }

    @classmethod
    def toggle_theme(cls):
        cls.current_theme = "light" if cls.current_theme == "dark" else "dark"

    @classmethod
    def get_theme(cls, screen_name):
        if screen_name == "home":
            return cls.themes["home"]
        elif screen_name == "encrypt":
            return cls.themes["encrypt_dark"] if cls.current_theme == "dark" else cls.themes["encrypt_light"]
        elif screen_name == "decrypt":
            return cls.themes["decrypt_dark"] if cls.current_theme == "dark" else cls.themes["decrypt_light"]
