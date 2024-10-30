from tkinter import *
root=Tk()
ent=Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
ent.pack()
ent.insert(0,"Введите ваше имя")
def myClick():
    wind=Label(root,text="Нажата кнопка!")
    wind.pack()
wind2=Button(root, text ="Нажми",command=myClick,fg="blue",bg="white")
wind2.pack()
root.mainloop()