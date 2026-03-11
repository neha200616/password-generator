from tkinter import *
import pyperclip
from backend import generate_password, check_strength


def create_password():

    length = int(length_entry.get())
    numbers = number_var.get()
    symbols = symbol_var.get()

    password = generate_password(length, numbers, symbols)

    result_entry.delete(0, END)
    result_entry.insert(0, password)

    strength = check_strength(password)
    strength_label.config(text="Strength: " + strength)


def copy_password():

    password = result_entry.get()
    pyperclip.copy(password)


root = Tk()
root.title("Cyber Password Generator")
root.geometry("400x350")
root.configure(bg="black")

title = Label(root, text="Password Generator", fg="lime", bg="black", font=("Arial",16))
title.pack(pady=10)

Label(root, text="Password Length", fg="white", bg="black").pack()

length_entry = Entry(root)
length_entry.pack()

number_var = BooleanVar()
Checkbutton(root, text="Include Numbers", variable=number_var, bg="black", fg="white").pack()

symbol_var = BooleanVar()
Checkbutton(root, text="Include Symbols", variable=symbol_var, bg="black", fg="white").pack()

Button(root, text="Generate Password", command=create_password, bg="lime").pack(pady=10)

result_entry = Entry(root, width=30)
result_entry.pack(pady=5)

Button(root, text="Copy Password", command=copy_password).pack()

strength_label = Label(root, text="Strength:", fg="yellow", bg="black")
strength_label.pack(pady=10)

root.mainloop()