print ("lo van dong")
print ("235752021610070")

import tkinter as tk

def create_form():
    window = tk.Tk()
    window.title("Thông tin cá nhân")

    label_ho_ten = tk.Label(window, text="Họ và tên:")
    label_ho_ten.pack()
    entry_ho_ten = tk.Entry(window)
    entry_ho_ten.pack()

    label_ngaysinh = tk.Label(window, text="Ngày sinh:")
    label_ngaysinh.pack()
    entry_ngaysinh = tk.Entry(window)
    entry_ngaysinh.pack()

    label_mssv = tk.Label(window, text="MSSV:")
    label_mssv.pack()
    entry_mssv = tk.Entry(window)
    entry_mssv.pack()

    label_nganh_hoc = tk.Label(window, text="Ngành học:")
    label_nganh_hoc.pack()
    entry_nganh_hoc = tk.Entry(window)
    entry_nganh_hoc.pack()

    button_submit = tk.Button(window, text="Gửi")
    button_submit.pack()

    window.mainloop()

if __name__ == "__main__":
    create_form()
