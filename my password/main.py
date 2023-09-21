from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# PASSWORD GENERATOR
def rand_pass():
    letters = random.randint(8, 10)
    symbols = random.randint(2, 4)
    nums = random.randint(2, 4)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symb = ["!", "@", "#", "$", "%", "^", "&", "*"]
    lett = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v",
            "b", "n", "m", "q", "w", "e", "r", "t", "y",
            "u", "i", "o", "p" "Q", "W", "E", "R", "T", "Y", "U", "I", "O",
            "P", "A", "S", "D", "F", "G", "H", "J", "K",
            "L", "Z", "X", "C", "V", "B", "N", "M"]

    password = []
    for char in range(1, letters + 1):
        ran_char = random.choice(lett)
        password += ran_char

    for sym in range(1, symbols + 1):
        ran_sym = random.choice(symb)
        password += ran_sym

    for num in range(1, nums + 1):
        ran_numb = random.choice(numbers)
        password += ran_numb

    random.shuffle(password)

    pasword = ""
    for char in password:
        pasword += char

    p = "".join(password)
    pass_ent.delete(0, END)
    pass_ent.insert(0, pasword)
    pyperclip.copy(p)


# SAVE PASSWORD


def save_pass():
    website = web_ent.get()
    email = user_ent.get()
    password = pass_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Unexpected error",
                             message="Please check all fields (empty field).")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Your details is: \nEmail: {email}"
                                               f"\nPassword: {password} \nAre you sure to "
                                               f"save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_ent.delete(0, END)
                pass_ent.delete(0, END)
        else:
            pass


def search():
    try:
        with open("data.json", "r") as file:
            sear = json.load(file)
        messagebox.showinfo(title=web_ent.get(), message=f"Your details is: \nEmail: {sear[web_ent.get()]['email']} "
                                                         f"\nPassword: {sear[web_ent.get()]['password']}")
    except KeyError:
        messagebox.showerror(title="No Data", message=f"This website: ({web_ent.get()}) is not found")


# UI SETUP
win = Tk()
win.title("Password Manager")
win.config(padx=50, pady=50, bg="lightcyan")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="lightcyan")
pass_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_photo)
canvas.grid(column=1, row=0)

web_lab = Label(text="Website:", pady=7, bg="lightcyan")
web_lab.grid(column=0, row=1)

web_ent = Entry(width=35)
web_ent.grid(column=1, row=1, columnspan=1)
web_ent.focus()

user_lab = Label(text="Email/Username:", pady=7, bg="lightcyan")
user_lab.grid(column=0, row=2)

user_ent = Entry(width=52)
user_ent.grid(column=1, row=2, columnspan=2)
user_ent.insert(END, "omartohamy2004@gmail.com")

pass_lab = Label(text="Password:", pady=7, bg="lightcyan")
pass_lab.grid(column=0, row=3)

pass_ent = Entry(width=32)
pass_ent.grid(column=1, row=3)

pass_butt = Button(text="Generate Password", bg="dodgerblue", fg="white", command=rand_pass)
pass_butt.grid(column=2, row=3)

pass_butt = Button(text="Add", width=44, bg="dodgerblue", fg="white", command=save_pass)
pass_butt.grid(column=1, row=4, columnspan=2)

pass_butt = Button(text="Search", width=11, fg='white', bg="dodgerblue", command=search)
pass_butt.grid(column=2, row=1, columnspan=1)

win.mainloop()
