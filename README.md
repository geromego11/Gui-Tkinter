# Tkinter Login Application

This is a simple graphical login application built using Python's Tkinter library. The application accepts a username and password and provides feedback based on the input. It also includes a "Show/Hide Password" feature for convenience.

## Features

- **Username and Password Input**: Users can input their credentials.
- **Show/Hide Password Toggle**: The password input is hidden by default, but users can toggle visibility using the "Show/Hide" button.
- **Basic Authentication**: Checks if the username and password are correct and displays appropriate messages.
  - Username: `Gerome`
  - Password: `admin`

## Requirements

- Python 3.x
- Tkinter (This comes pre-installed with Python on most systems)

## How to Run the Application

1. Make sure Python 3 is installed on your machine. If not, you can download it from [here](https://www.python.org/downloads/).
2. Copy the Python script below and save it as `login_app.py`:

    ```python
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
    ```

3. Open a terminal or command prompt in the directory where the script is saved.
4. Run the script with the following command:

    ```bash
    python login_app.py
    ```

## How to Use

1. Run the application as shown in the instructions above.
2. Enter the following credentials:
   - **Username**: `Gerome`
   - **Password**: `admin`
3. Click the "Login" button to check if the credentials are correct.
4. Use the "Show/Hide" button next to the password field to toggle password visibility.

## Screenshots

- A simple interface with username, password, and login button.
- A toggle button to show or hide the password.

## License

This project is open source and available under the [MIT License](LICENSE).

