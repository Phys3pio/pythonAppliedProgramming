import tkinter as tk
from tkinter import messagebox
class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.grid(row=0, column=0)


        self.principal = tk.DoubleVar()
        self.rate = tk.DoubleVar()
        self.years = tk.IntVar()
        self.amount = tk.StringVar(value="0.00")

        # Создание виджетов
        labelPrincipal = tk.Label(self, text="Principal:", underline=0, anchor=tk.W)
        entryPrincipal = tk.Entry(self, textvariable=self.principal)

        labelRate = tk.Label(self, text="Rate (%):", underline=0, anchor=tk.W)
        scaleRate = tk.Scale(self, variable=self.rate, orient=tk.HORIZONTAL, from_=0, to=100, resolution=0.01, command=self.updateUi)

        labelYears = tk.Label(self, text="Years:", underline=0, anchor=tk.W)
        spinboxYears = tk.Spinbox(self, textvariable=self.years, from_=1, to=30, increment=1, command=self.updateUi)

        labelActualAmount = tk.Label(self, text="Actual Amount:", underline=0, anchor=tk.W)
        actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)

        # Размещение виджетов на сетке
        labelPrincipal.grid(row=0, column=0, sticky=tk.W)
        entryPrincipal.grid(row=0, column=1, sticky=tk.EW)

        labelRate.grid(row=1, column=0, sticky=tk.W)
        scaleRate.grid(row=1, column=1, sticky=tk.EW)

        labelYears.grid(row=2, column=0, sticky=tk.W)
        spinboxYears.grid(row=2, column=1, sticky=tk.EW)

        labelActualAmount.grid(row=3, column=0, sticky=tk.W)
        actualAmountLabel.grid(row=3, column=1, sticky=tk.EW)

        # Обработка нажатия клавиши Escape для выхода
        self.parent.bind("<Escape>", self.quit)

        # Первоначальный расчет
        self.updateUi()

    def updateUi(self, *ignore):
        # Расчет актуального значения
        p = self.principal.get()
        r = self.rate.get()
        y = self.years.get()
        a = round(p * (1 + r / 100) ** y, 2)
        self.amount.set(str(a))

        messagebox.showinfo("Success", "Пересчет выполнен успешно!")

    def quit(self, event=None):
        self.parent.destroy()

    def increase_years(self):
        current_years = self.years.get()
        self.years.set(current_years + 1)

    def decrease_years(self):
        current_years = self.years.get()
        if current_years > 1:
            self.years.set(current_years - 1)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Close Window", command=self.quit)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Increase Years", command=self.increase_years)
        self.context_menu.add_command(label="Decrease Years", command=self.decrease_years)

        self.parent.bind("<Button-3>", self.popup)

    def popup(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.context_menu.grab_release()