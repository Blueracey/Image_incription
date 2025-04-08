from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.core.clipboard import Clipboard
from tkinter import filedialog, Tk
import shutil
import os

from Utils.utils import generate_random_pattern, get_image
from Utils.encryption import encript


class EncryptScreen(Screen):
    selected_file = StringProperty("No image selected")
    encrypted_file = StringProperty("")
    reuse_key = BooleanProperty(False)

    def open_file_chooser(self):
        from Utils.file_chooser import FileChooserPopup
        popup = FileChooserPopup(self.set_selected_file)
        popup.open()

    def set_selected_file(self, file_path):
        self.selected_file = file_path
        self.ids.selected_image.source = file_path

    def toggle_reuse_key(self):
        self.reuse_key = not self.reuse_key
        self.ids.reuse_key_button.text = "Reusing Key" if self.reuse_key else "Not Reusing Key"
        if not self.reuse_key:
            App.get_running_app().reused_pattern = None

    def encrypt_message(self):
        if not self.selected_file or self.selected_file == "No image selected":
            print("Please select an image first.")
            return

        message = self.ids.message_input.text
        if not message:
            print("Please enter a message to encrypt.")
            return

        app = App.get_running_app()

        if self.reuse_key and app.reused_pattern:
            pattern = app.reused_pattern
        else:
            pattern = generate_random_pattern()
            if self.reuse_key:
                app.reused_pattern = pattern

        img = get_image(self.selected_file)
        output_path = "encrypted_output.png"

        encript(img, message, pattern)

        self.ids.key_output.text = f"Key Used: {pattern}"
        self.ids.encrypted_image.source = output_path
        self.encrypted_file = output_path
        print("Encryption successful!")

    def show_full_image(self, path):
        if not path:
            return
        image = KivyImage(source=path, allow_stretch=True)
        layout = BoxLayout()
        layout.add_widget(image)
        popup = Popup(title="Full Image Preview", content=layout,
                      size_hint=(0.9, 0.9), auto_dismiss=True)
        popup.open()

    def copy_key_to_clipboard(self):
        key_text = self.ids.key_output.text.replace("Key Used: ", "")
        Clipboard.copy(key_text)
        print("Key copied to clipboard!")

    def download_encrypted_image(self):
        if not self.encrypted_file:
            print("No encrypted image to download.")
            return

        root = Tk()
        root.withdraw()
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")],
            title="Save Encrypted Image As"
        )
        root.destroy()

        if save_path:
            shutil.copy(self.encrypted_file, save_path)
            print(f"Image saved to: {save_path}")
