from tkinter import *
from tkinter import messagebox

# ------------------------
# Functions
# ------------------------

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task first.")

def clear_tasks():
    answer = messagebox.askyesno("Clear", "Delete all tasks?")
    if answer:
        task_listbox.delete(0, END)

# ------------------------
# GUI
# ------------------------

window = Tk()
window.title("To-Do List")
window.geometry("400x500")
window.resizable(False, False)

title = Label(window, text="TO-DO LIST", font=("Arial", 20, "bold"))
title.pack(pady=10)

task_entry = Entry(window, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

task_listbox = Listbox(window, width=40, height=12, font=("Arial", 12))
task_listbox.pack(pady=10)

delete_button = Button(window, text="Delete Selected", width=20, command=delete_task)
delete_button.pack(pady=5)

clear_button = Button(window, text="Clear All", width=20, command=clear_tasks)
clear_button.pack(pady=5)

window.mainloop()
