import tkinter as tk
from tkinter import ttk
import tkinter.font as font

def calculate_centimeters(e):
    try:
        metres = float(metres_value.get())
        centimetres = metres * 100
        centimetres_value.set(f"{centimetres:.2f}")
    except:
        pass
    


root = tk.Tk()
root.title("Distance Convertor")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

font.nametofont("TkDefaultFont").configure(family="terminal",size=15)


root.bind("<Return>", calculate_centimeters)
root.bind("<KP_Enter>", calculate_centimeters)
metres_value = tk.StringVar()
centimetres_value = tk.StringVar()

main = ttk.Frame(root, padding=(30,15))
main.grid()

metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, justify="center", textvariable=metres_value, font=("terminal",15))
metres_input.focus()
centi_metres_label = ttk.Label(main, text="CentiMetres:")
centimetres_display = ttk.Label(main, text="CentiMetres shown here...", textvariable=centimetres_value)

calc_button = ttk.Button(main, text="Calculate",command=calculate_centimeters)


metres_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
metres_input.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

centi_metres_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
centimetres_display.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

calc_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)


root.mainloop()