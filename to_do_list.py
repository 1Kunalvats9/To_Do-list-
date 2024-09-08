import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task != "":
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Window size
root.geometry("400x400")

# Create the task entry field
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Create buttons for task operations
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", width=20, command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
clear_button.pack(pady=5)

# Create the task listbox
listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

