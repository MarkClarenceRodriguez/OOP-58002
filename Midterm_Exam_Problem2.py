from tkinter import *

root = Tk()
root.title("My Full Name")
root.geometry("400x300")
root.config(bg="white")

title = Label(root, text="My Full Name", font=("Verdana", 16), fg="red")
title.pack(pady=10)

given_name_label = Label(root, text="Enter Given Name:", font=("Verdana", 12), fg="red", anchor="w")
given_name_label.pack()

given_name_entry = Entry(root, font=("Verdana", 12))
given_name_entry.pack(pady=5)

middle_name_label = Label(root, text="Enter Middle Name:", font=("Verdana", 12), fg="red", anchor="w")
middle_name_label.pack()

middle_name_entry = Entry(root, font=("Verdana", 12))
middle_name_entry.pack(pady=5)

last_name_label = Label(root, text="Enter Last Name:", font=("Verdana", 12), fg="red", anchor="w")
last_name_label.pack()

last_name_entry = Entry(root, font=("Verdana", 12))
last_name_entry.pack(pady=5)

full_name_label = Label(root, text="My Full Name is:", font=("Verdana", 12), fg="red", anchor="w")
full_name_label.pack()

full_name_entry = Entry(root, font=("Verdana", 12), fg="red")
full_name_entry.pack(pady=5)

def show_full_name():
    full_name = f"{last_name_entry.get()}, {given_name_entry.get()} {middle_name_entry.get()}"
    full_name_entry.delete(0, END)

    full_name_entry.insert(0, full_name)

show_button = Button(root, text="Show Full Name", font=("Verdana", 12), command=show_full_name)
show_button.pack(pady=10)

def clear_entries():
    given_name_entry.delete(0, END)
    middle_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    full_name_entry.delete(0, END)

clear_button = Button(root, text="Clear All", font=("Verdana", 12), command=clear_entries)
clear_button.pack(pady=10)

root.mainloop()
