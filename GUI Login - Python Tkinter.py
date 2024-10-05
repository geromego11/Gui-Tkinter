from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        messagebox.showinfo("", "Blank Not Allowed")
    elif username == "Gerome" and password == "admin":
        messagebox.showinfo("", "Login Success")
    else:
        messagebox.showinfo("", "Incorrect username or password")

def toggle_password():
    # Toggle between showing and hiding the password
    if entry2.cget('show') == '':
        entry2.config(show='*')
        toggle_btn.config(text='Show')
    else:
        entry2.config(show='')
        toggle_btn.config(text='Hide')

root = Tk()
root.title("Login")
root.geometry("300x250")

# Username label and entry
Label(root, text="Username").place(x=20, y=20)
entry1 = Entry(root, bd=5)
entry1.place(x=140, y=20)

# Password label and entry (with default hidden state)
Label(root, text="Password").place(x=20, y=70)
entry2 = Entry(root, bd=5, show='*')
entry2.place(x=140, y=70)

# Toggle password visibility button
toggle_btn = Button(root, text="Show", command=toggle_password)
toggle_btn.place(x=260, y=70)

# Login button
Button(root, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=150)

root.mainloop()
