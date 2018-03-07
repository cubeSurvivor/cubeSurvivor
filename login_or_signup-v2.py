def printtext():
    global e
    string = e.get() 
    print string   

from Tkinter import *
root = Tk()

root.title('Username')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Create Username',command=printtext)
b.pack(side='bottom')
root.mainloop()
