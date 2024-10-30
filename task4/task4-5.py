import tkinter as tk
class Table(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.count = 10
        self.button1 = tk.Button(self, text="1", width=5, command=self.new_window)
        self.button1.grid(row=0,column=0)
        self.button2 = tk.Button(self, text="2", width=5, command=self.new_info_window)
        self.button2.grid(row=1,column=0)
        self.button3 = tk.Button(self, text="3", width=5, command=self.new_window)
        self.button3.grid(row=2,column=0)
        self.button4 = tk.Button(self, text="4", width=5, command=self.new_info_window)
        self.button4.grid(row=3,column=0)
        self.button5 = tk.Button(self, text="5", width=5, command=self.new_window)
        self.button5.grid(row=0,column=1)
        self.button6 = tk.Button(self, text="6", width=5, command=self.new_info_window)
        self.button6.grid(row=1,column=1)
        self.button7 = tk.Button(self, text="7", width=5, command=self.new_window)
        self.button7.grid(row=2,column=1)
        self.button8 = tk.Button(self, text="8", width=5, command=self.new_info_window)
        self.button8.grid(row=3,column=1)
        self.button9 = tk.Button(self, text="9", width=5, command=self.new_window)
        self.button9.grid(row=0,column=2)
        self.button0 = tk.Button(self, text="0", width=5, command=self.new_info_window)
        self.button0.grid(row=1,column=2)
    def new_info_window(self):
        InfoWindow(self,"inform")
    def new_window(self):
        self.app=Demo2()
        self.app.title("okno #"+str(self.count))
        self.app.geometry("300x100+200+100")
        self.app.mainloop()
def main():
    app=Table()
    app.title("okno vizu")
    app.geometry("400x400+200+100")
    app.mainloop()
if __name__=='__main__':
    main()