import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry('600x400')

# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
# ttk.Label(root, text="hello", padding=20).pack()
# ttk.Separator(root, orient="horizontal").pack(fill="x")
# ttk.Label(root, text="good", padding=20).pack()


# select_option1 = tk.StringVar()
# select_option2 = tk.StringVar()
# def print_current_selection():
#     print(select_option1.get())
#     print(select_option2.get())
    
    

# check_button = ttk.Checkbutton(root, text="check",variable=select_option1, command=print_current_selection, onvalue="selected", offvalue="deseleted")
# check_button.pack()
# check_button = ttk.Checkbutton(root, text="check",variable=select_option2, command=print_current_selection, onvalue="selected", offvalue="deseleted")
# check_button.pack()
# check_button["state"] = "disabled"

# clicked = {
#     'option_1':False,
#     'option_2':False,
# }

# def selected():
#     if not clicked["option_1"]:
#         clicked["option_1"] = True
#         print(select_option.get())
#     else:
#         select_option.set("")
#         clicked["option_1"] = False
# select_option = tk.StringVar()

# option_1 = ttk.Radiobutton(root, text="male", variable=select_option, value="male", command= selected)
# option_1.pack()



# option_2 = ttk.Radiobutton(root, text="female", variable=select_option, value="female", command= selected)
# option_2.pack()

# def handle_selection(e):
#     print(selected_weekday.get())
    


# week_days = ("Mon","Tue","Wed")
# selected_weekday = tk.StringVar(value=week_days[0])
# weekday = ttk.Combobox(root, textvariable=selected_weekday)
# weekday["values"] =week_days 
# weekday.pack()
# weekday["state"] = "readonly"

# weekday.bind("<<ComboboxSelected>>", handle_selection)

# def handle_selection(e):
#     index = langs_select.curselection()
#     print(index)
#     for i in index:
#         print(langs_select.get(i))

# programming_languages = ("c++", "c#", "java", "javascript", "python")
# langs = tk.StringVar(value=programming_languages)

# langs_select = tk.Listbox(root, listvariable=langs,height=5)
# langs_select.pack()
# langs_select["selectmode"] = "extended"
# # langs_select["selectmode"] = "browse"
# langs_select.bind("<<ListboxSelect>>", handle_selection)

# init_value = tk.IntVar(value=20)
# # spin_box = ttk.Spinbox(root, from_=0, to=50, textvariable=init_value,wrap=True)
# spin_box = ttk.Spinbox(root, values=(5,10,15,20), textvariable=init_value,wrap=True)
# spin_box.pack()

def handle_scale(e):
    print(c.get())

c = tk.IntVar()
scale = ttk.Scale(root,from_=0, to=10,  orient="horizontal",variable=c, command=handle_scale)
scale.pack()



root.mainloop()
