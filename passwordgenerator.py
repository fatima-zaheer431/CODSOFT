import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

# Function to generate a password
def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += "-_"

    if not characters:
        return "Character set is empty."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate and display a password
def generate_and_display_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            messagebox.showwarning("Warning", "Password length must be greater than 0.")
            return

        use_lowercase = lowercase_var.get()
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        generated_password = generate_password(
            password_length, use_lowercase, use_uppercase, use_digits, use_special_chars)

        password_display.config(text=f"Generated Password: {generated_password}", foreground="blue", font=("Helvetica", 12, "bold"))

    except ValueError:
        messagebox.showwarning("Warning", "Invalid input for password length.")

app = tk.Tk()
app.title("Password Generator")

# Create input field for password length
length_label = ttk.Label(app, text="Password Length:", font=("Helvetica", 12))
length_label.pack()
length_entry = ttk.Entry(app, font=("Helvetica", 12))
length_entry.pack()

# Create checkboxes for complexity options
lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(app, text="Include lowercase letters", variable=lowercase_var, style="Checkbutton.TCheckbutton")
lowercase_check.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(app, text="Include uppercase letters", variable=uppercase_var, style="Checkbutton.TCheckbutton")
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(app, text="Include digits", variable=digits_var, style="Checkbutton.TCheckbutton")
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = ttk.Checkbutton(app, text="Include - and _", variable=special_chars_var, style="Checkbutton.TCheckbutton")
special_chars_check.pack()

# Create a button to generate and display the password
generate_button = ttk.Button(app, text="Generate Password", command=generate_and_display_password, style="TButton", padding=5)
generate_button.pack()

# Create a label to display the generated password
password_display = ttk.Label(app, text="", font=("Helvetica", 14))
password_display.pack()

# Configure the styles for Checkbuttons and the button
style = ttk.Style()
style.configure("Checkbutton.TCheckbutton", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Run the application
app.mainloop()
