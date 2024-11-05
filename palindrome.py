import tkinter as tk
from tkinter import messagebox
from palindrome_checker import is_palindrome

def validate_palindrome():
    input_string = entry.get()
    if is_palindrome(input_string):
        messagebox.showinfo("Resultado", "Cadena válida")
    else:
        messagebox.showwarning("Resultado", "Cadena no válida")

root = tk.Tk()
root.title("Máquina de Palíndromos")
root.configure(bg='lightblue')

frame = tk.Frame(root, bg='lightblue')
frame.pack(pady=20)

label = tk.Label(frame, text="Introduce una cadena:", bg='lightblue')
label.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(pady=10)

validate_button = tk.Button(frame, text="Validar", command=validate_palindrome, bg='blue', fg='white')
validate_button.pack(pady=10)

root.mainloop()