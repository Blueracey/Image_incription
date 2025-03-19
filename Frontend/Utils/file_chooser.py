from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

class FileChooserPopup(Popup):
    """Pop-up for selecting an image file."""
    selected_file = StringProperty("")

    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title = "Select Image"
        self.size_hint = (0.9, 0.9)
        
        layout = BoxLayout(orientation="vertical")
        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)
        
        select_button = Button(text="Select", size_hint_y=0.1)
        select_button.bind(on_release=self.select_file)
        layout.add_widget(select_button)
        
        self.callback = callback
        self.content = layout

    def select_file(self, instance):
        if self.file_chooser.selection:
            self.selected_file = self.file_chooser.selection[0]
            self.callback(self.selected_file)
        self.dismiss()
