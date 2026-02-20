import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box (Display)
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Function to add value
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear screen
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=calculate)
    elif text == "C":
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=clear)
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: button_click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Run app
root.mainloop()