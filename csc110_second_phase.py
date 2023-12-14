
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Page CSC 110")
window.geometry("340x440")
# window.configure(bg='#333333')


def login():
    username_1 = "root"
    password_1 = "password"

    username_2 = "johndoe"
    password_2 = "1234"

    if username_entry.get() == username_1 and password_entry.get() == password_1:
        messagebox.showinfo(title="Login status", message="Welcome administrator!")
    elif username_entry.get() == username_2 and password_entry.get() == password_2:
        messagebox.showinfo(title="Login status", message="Login successful!")
    else:
        messagebox.showinfo(title="Login status", message="Invalid username or password")


frame = tkinter.Frame()

# creating widgets for password and login
# login_label = tkinter.Label(frame, text="Login")
username_label = tkinter.Label(frame, text="Username:")
username_entry = tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show="*")
password_label = tkinter.Label(frame, text="Password:")
login_button = tkinter.Button(frame, text="Login", command=login)

# placing the widgets on the screen
# login_label.grid(row=0, column=0, columnspan=2, pady=10)
username_label.grid(row=2, column=0, pady=10)
username_entry.grid(row=2, column=1)
password_entry.grid(row=3, column=1)
password_label.grid(row=3, column=0)
login_button.grid(row=4, column=0, columnspan=2, pady=10)

frame.pack()

window.mainloop()
