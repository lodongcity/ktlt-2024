print ("lo van dong")
print ("235752021610070")

import tkinter as tk

def show_selected():
    selected = var.get()
    label_result.config(text=f"Bạn đã chọn: {selected}")

window = tk.Tk()
window.title("Chọn một số")

var = tk.IntVar()
radio1 = tk.Radiobutton(window, text="Số 1", variable=var, value=1)
radio2 = tk.Radiobutton(window, text="Số 2", variable=var, value=2)
radio3 = tk.Radiobutton(window, text="Số 3", variable=var, value=3)

button = tk.Button(window, text="Click Me", command=show_selected)

label_result = tk.Label(window)

radio1.pack()
radio2.pack()
radio3.pack()
button.pack()
label_result.pack()

window.mainloop()
