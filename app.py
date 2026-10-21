import tkinter as tk
from datetime import date

app = tk.Tk()
app.title("age app")
app.geometry("400x300")

tk.Label(app, text="birth year:").pack(pady=10)
entry = tk.Entry(app)
entry.pack()

result = tk.Label(app, text="")
result.pack(pady=10)

def calc():
    year = int(entry.get())
    age = date.today().year - year
    result.config(text=f"you are {age} years old")
   
tk.Button(app, text="calculate", command=calc).pack(pady=10)
   
app.mainloop()
