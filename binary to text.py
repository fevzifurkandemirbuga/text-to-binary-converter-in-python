import tkinter as tk
from dictionaries import BinaryToText, TextToBinary


def convert():
    text = textLeft.get("1.0", "end-1c")
    binary_text = ""
    textRight.delete('1.0', tk.END)
    if radio_state.get() == 1:
        for i in text:
            binary_text += f"{TextToBinary[i]} "
        textRight.insert(tk.END, binary_text)
    else:
        binary_list = text.split(" ")
        for i in binary_list:
            binary_text += BinaryToText[i]
        textRight.insert(tk.END, binary_text)


window = tk.Tk()
window.config(padx=50, pady=100)
textLeft = tk.Text(height=20, width=36)
textLeft.focus()
textRight = tk.Text(height=20, width=36)
button = tk.Button(text="convert", font=("ariel", 20, "bold"), command=convert)

radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Text To Binary", value=1, variable=radio_state)
radiobutton2 = tk.Radiobutton(text="Binary To Text", value=2, variable=radio_state)

textLeft.grid(column=0, row=1)
textRight.grid(column=4, row=1)
button.grid(column=2, row=2)
radiobutton2.grid(column=3, row=0)
radiobutton1.grid(column=1, row=0)
window.mainloop()
