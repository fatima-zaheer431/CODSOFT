import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to update a selected task in the list
def update_task():
    try:
        selected_task_index = task_list.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to remove a selected task from the list
def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Set a custom font family for the application
custom_font = ("Helvetica", 12)

# Create an input field for adding/updating tasks with custom font
task_entry = tk.Entry(app, width=40, font=custom_font)
task_entry.pack(pady=10)

# Create a button to add tasks with custom font and appearance
add_button = tk.Button(app, text="Add Task", width=15, command=add_task, font=custom_font, bg='lightgreen', relief='ridge')
add_button.pack(side=tk.LEFT, padx=5)

# Create a button to update tasks with custom font and appearance
update_button = tk.Button(app, text="Update Task", width=15, command=update_task, font=custom_font, bg='lightblue', relief='ridge')
update_button.pack(side=tk.LEFT, padx=5)

# Create a button to remove tasks with custom font and appearance
remove_button = tk.Button(app, text="Remove Task", width=15, command=remove_task, font=custom_font, bg='indianred', relief='ridge')
remove_button.pack(side=tk.LEFT, padx=5)

# Create a listbox to display tasks with custom font and select mode
task_list = tk.Listbox(app, width=40, selectbackground='lightblue', font=custom_font, selectmode=tk.SINGLE, bg='white')
task_list.pack(pady=10)

# Run the application
app.mainloop()
