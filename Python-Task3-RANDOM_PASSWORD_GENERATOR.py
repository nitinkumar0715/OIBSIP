import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Length should be at least 4")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x220")
root.configure(bg="#1e1e2f")

tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=10)

tk.Label(
    root,
    text="Password Length",
    bg="#1e1e2f",
    fg="white"
).pack()

length_entry = tk.Entry(root, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white"
).pack(pady=10)

password_entry = tk.Entry(root, width=30, justify="center", font=("Arial", 12))
password_entry.pack(pady=10)

root.mainloop()