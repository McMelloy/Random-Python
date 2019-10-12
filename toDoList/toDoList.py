import tkinter


def add():
    tasks.insert("end",txt_entry.get())
    update()


def done():
    for i in tasks:
        if i == txt_entry.get():
            print ("Found")
            del tasks[tasks.index(i)]
            update()


def update():
    list.delete(0,"end")
    for i in tasks:
        list.insert("end", i)


def clear():
    list.delete(0,"end")


root = tkinter.Tk()
root.title("To-Do list")
root.geometry("200x300")

tasks = ["Do this", "Do that", "Do everything"]

lbl_title = tkinter.Label(root, text="Ave Todd Howard!")
lbl_title.pack()

txt_entry = tkinter.Entry(root, width=20)
txt_entry.pack()

btn_add = tkinter.Button(root, text="Add", command=add)
btn_add.pack()

btn_done = tkinter.Button(root, text="Done", command=done)
btn_done.pack()

#btn_update = tkinter.Button(root, text="Update", command=update)
#btn_update.pack()

btn_clear = tkinter.Button(root, text="Clear all", command=clear)
btn_clear.pack()


list = tkinter.Listbox(root, width = 30, height = 10)
list.pack()


update()
root.mainloop()

