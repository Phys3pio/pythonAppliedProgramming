import os
import sys
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path


class PhotoViewer(Tk):
    def __init__(self):
        super().__init__()
        self.title("Photo Viewer")
        self.geometry("800x600")


        self.path = Path(__file__).parent.resolve()
        image_folder_path = self.path.joinpath("images")


        icon_file = self.path.joinpath("test_axe.ico").resolve()
        self.iconbitmap(icon_file)


        self.images = []
        for file in os.listdir(image_folder_path):
            img_path = image_folder_path.joinpath(file)
            img = Image.open(img_path)
            photo = ImageTk.PhotoImage(img)
            self.images.append(photo)


        self.current_index = 0


        self.photo_label = Label(self)
        self.update_photo()


        self.info_label = Label(
            self, text=f"1/{len(self.images)}",
            bd=1, relief=SUNKEN, anchor=E
        )
        self.info_label.grid(row=1, column=0, sticky=W + E)


        self.button_back = Button(self, text="<", command=self.back)
        self.button_forward = Button(self, text=">", command=lambda: self.forward(1))
        self.button_exit = Button(self, text="Выход", command=self.destroy)


        self.photo_label.grid(row=0, column=0)
        self.button_back.grid(row=1, column=0, sticky=W)
        self.button_forward.grid(row=1, column=0, sticky=E)
        self.button_exit.grid(row=1, column=0, pady=5)


        if len(self.images) <= 1:
            self.button_back.config(state=DISABLED)

    def update_photo(self):
        self.photo_label.configure(image=self.images[self.current_index])
        self.photo_label.image = self.images[self.current_index]

    def back(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.update_photo()
            self.info_label.config(text=f"{self.current_index + 1}/{len(self.images)}")
            self.button_forward.config(state=NORMAL)
            if self.current_index == 0:
                self.button_back.config(state=DISABLED)

    def forward(self, step):
        if self.current_index < len(self.images) - 1:
            self.current_index += step
            self.update_photo()
            self.info_label.config(text=f"{self.current_index + 1}/{len(self.images)}")
            self.button_back.config(state=NORMAL)
            if self.current_index == len(self.images) - 1:
                self.button_forward.config(state=DISABLED)


if __name__ == "__main__":
    app = PhotoViewer()
    app.mainloop()