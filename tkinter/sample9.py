from tkinter import Tk, Frame, Menu


# root window
root = Tk()
root.geometry('320x150')
root.title('Menu Demo')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

root.mainloop()



# askquestion.YES = 'blalalalal'
# askquestion.NO = 'no'
# button = askquestion("question", "Are you sure?")

# print(button)

# passw = Entry(root, width=16, show='*')
# passw.pack()

# def enter(event):
#     print(f"Entered: {event.x} {event.y}")
    
    
# frame = Frame(root, width=150, height=150)
# frame.bind('<Any-Enter>', enter)
# frame.bind('<Button-1>', enter)
# frame.bind('<Button-2>', enter)
# frame.bind('<B2-Motion>', enter)
# frame.bind('<KeyPress-back-slash>', enter)
# frame.bind('<KeyPress-back-slash>', enter)
# frame.pack()

root.mainloop()