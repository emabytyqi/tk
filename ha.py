import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
label = tk.Label(root, text="Miresevini ne kalkulator", font=("arial", 18))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(root, height=3)
textbox.pack()

root.mainloop()

