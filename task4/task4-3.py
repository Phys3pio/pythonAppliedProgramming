from tkinter import *
root=Tk()
def myClick():
    wind=Label(root,text="Нажата кнопка!")
    wind.pack()
wind2=Button(root, text ="Нажми",command=myClick,fg="blue",bg="white")
wind2.pack()
root.mainloop()