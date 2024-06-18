import tkinter as tk

window = tk.Tk()
window.geometry("514x1000")
window.resizable(False, False)
c = tk.Canvas(width=514, height=1000, background="#B0C447", highlightthickness=0)
c.pack()


def placeholder(entry, text):
    c.tk.call("focus", window)
    if entry.get() == '':
        entry.insert(tk.END, text)
        entry.config(fg="grey")


def return_placeholders(entry=None, text=None):
    c.tk.call("focus", window)
    placeholder(name, ' First and last name')
    placeholder(email, ' example@domain.com')
    placeholder(phone, ' Eg. +447500000000')
    if entry is not None:
        if entry.get() == text:
            entry.delete(0, tk.END)
        entry.config(fg="black")


c.create_text(20, 20, font=('Times New Roman', 16), text="Step 1: Your details", anchor=tk.NW)
c.create_rectangle(20, 60, 494, 120, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 125, 494, 185, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 190, 494, 250, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_text(30, 80, font=('Times New Roman', 14), text='Name', anchor=tk.NW)
c.create_text(30, 145, font=('Times New Roman', 14), text='Email', anchor=tk.NW)
c.create_text(30, 210, font=('Times New Roman', 14), text='Phone', anchor=tk.NW)

c.bind('<Button-1>', lambda event: return_placeholders())

name = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='grey', highlightthickness=0, border=0)
name.place(width=240, height=35, anchor=tk.NW, x=170, y=72)
placeholder(name, ' First and last name')
name.bind('<Button-1>', lambda event: return_placeholders(name, ' First and last name'))
name.bind('<Return>', lambda event: placeholder(name, ' First and last name'))

email = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='grey', highlightthickness=0, border=0)
email.place(width=240, height=35, anchor=tk.NW, x=170, y=137)
placeholder(email, ' example@domain.com')
email.bind('<Button-1>', lambda event: return_placeholders(email, ' example@domain.com'))
email.bind('<Return>', lambda event: placeholder(email, ' example@domain.com'))

phone = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='grey', highlightthickness=0, border=0)
phone.place(width=240, height=35, anchor=tk.NW, x=170, y=202)
placeholder(phone, ' Eg. +447500000000')
phone.bind('<Button-1>', lambda event: return_placeholders(phone, ' Eg. +447500000000'))
phone.bind('<Return>', lambda event: placeholder(phone, ' Eg. +447500000000'))

c.create_text(20, 270, font=('Times New Roman', 16), text="Step 2: Delivery address", anchor=tk.NW)
c.create_rectangle(20, 310, 494, 460, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 465, 494, 525, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 530, 494, 590, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_text(30, 330, font=('Times New Roman', 14), text='Address', anchor=tk.NW)
c.create_text(30, 485, font=('Times New Roman', 14), text='Post code', anchor=tk.NW)
c.create_text(30, 550, font=('Times New Roman', 14), text='Country', anchor=tk.NW)

address = tk.Text(font=('Times New Roman', 14, 'italic'), fg='black', highlightthickness=0, border=0)
address.place(width=240, height=125, anchor=tk.NW, x=170, y=322)

post = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='black', highlightthickness=0, border=0)
post.place(width=240, height=35, anchor=tk.NW, x=170, y=477)

country = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='black', highlightthickness=0, border=0)
country.place(width=240, height=35, anchor=tk.NW, x=170, y=542)

c.create_text(20, 610, font=('Times New Roman', 16), text="Step 3: Card details", anchor=tk.NW)
c.create_rectangle(20, 650, 494, 730, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 735, 494, 795, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 800, 494, 860, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_rectangle(20, 865, 494, 925, fill="#C9D584", outline="#EAEDCF", width=2)
c.create_text(30, 665, font=('Times New Roman', 14), text='Card type', anchor=tk.NW)
c.create_text(30, 755, font=('Times New Roman', 14), text='Card number', anchor=tk.NW)
c.create_text(30, 820, font=('Times New Roman', 14), text='Security code', anchor=tk.NW)
c.create_text(30, 885, font=('Times New Roman', 14), text='Name of card', anchor=tk.NW)

card1 = tk.Radiobutton(bg="#C9D584")
card1.place(anchor=tk.NW, x=50, y=695)

card2 = tk.Radiobutton(bg="#C9D584")
card2.place(anchor=tk.NW, x=180, y=695)

card3 = tk.Radiobutton(bg="#C9D584")
card3.place(anchor=tk.NW, x=310, y=695)

card = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='black', highlightthickness=0, border=0)
card.place(width=240, height=35, anchor=tk.NW, x=170, y=747)

code = tk.Entry(font=('Times New Roman', 14, 'italic'), fg='black', highlightthickness=0, border=0)
code.place(width=240, height=35, anchor=tk.NW, x=170, y=812)

window.mainloop()
