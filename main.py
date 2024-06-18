import tkinter as tk
import ttkbootstrap as ttk

def convert():
    input_val = entry_int.get()
    output_val = input_val * 1.8 + 32
    output_string.set(f'{output_val} \u00b0F')

# window
window = ttk.Window(themename='journal')
window.title('Temperature Converter')
window.geometry('500x500')

# title
title_label = ttk.Label(master=window, text='Celcius to Fahrenheit', font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    font='Calibri 24',
    textvariable=output_string
)
output_label.pack(pady=5)

# run
window.mainloop()
