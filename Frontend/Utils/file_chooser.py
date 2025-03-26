from tkinter import Tk, filedialog

class FileChooserPopup:
    def __init__(self, on_file_selected):
        self.on_file_selected = on_file_selected

    def open(self):
        root = Tk()
        root.withdraw()  #Hide main window
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        root.destroy()
        if file_path:
            self.on_file_selected(file_path)
