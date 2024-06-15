import tkinter as tk

window = tk.Tk()
window.geometry("514x818")
window.resizable(False, False)
c = tk.Canvas(width=514, height=818, background="#B0C447")
c.pack()

c.create_text(20, 20, font='TimesNewRoman 16', text="Step 1: Your details", anchor=tk.NW)
c.create_rectangle(20, 60, 494, 120, fill="#C9D584", outline="#EAEDCF", width=2)


window.mainloop()
