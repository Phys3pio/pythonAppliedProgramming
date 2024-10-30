import tkinter as tk
from mainWindow import MainWindow
from pathlib import Path


root = tk.Tk()

icon_file = Path(__file__).parent.joinpath("interest.ico").resolve()
root.iconbitmap(icon_file)

root.title("Interest Calculator")

window = MainWindow(root)

root.mainloop()