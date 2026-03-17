import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To_do_List")
root.geometry("900x900")
root.resizable(False, False)
root.config(bg="skyblue")

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_complete():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        if not task.startswith("[DONE] "):
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, "[DONE] " + task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

input_frame = tk.Frame(root, bg="white")
input_frame.grid(pady=20)
input_frame.config(bg="white")

task_label = tk.Label(input_frame, text="Enter Task:", bg="white", fg="black", font=("Arial", 18))
task_label.grid(row=0, column=0, padx=10)

task_entry = tk.Entry(input_frame, width=40, bg="white", fg="black", font=("Arial", 18))
task_entry.grid(row=0, column=1, padx=10)

add_button = tk.Button(input_frame, text="Add Task", command=add_task, bg="yellow", font=("Arial", 18))
add_button.grid(row=0, column=2, padx=10)
add_button.config(bg="yellow", font=("Arial", 18))

list_frame = tk.Frame(root, bg="black")
list_frame.grid(pady=20)

task_listbox = tk.Listbox(list_frame, width=60, height=15, bg="white", fg="black", font=("Arial", 18))
task_listbox.grid()

button_frame = tk.Frame(root, bg="black")
button_frame.grid(pady=20)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="yellow", font=("Arial", 18))
delete_button.grid(row=0, column=0, padx=10)
delete_button.config(bg="yellow", font=("Arial", 18))

complete_button = tk.Button(button_frame, text="Mark Complete", command=mark_complete, bg="yellow", font=("Arial", 18))
complete_button.grid(row=0, column=1, padx=10)
complete_button.config(bg="yellow", font=("Arial", 18))


root.mainloop()