from tkinter import *

def clicked():
    res =f'Hello {txt.get()}'
    lbl_welcome.configure(text=res)

window = Tk()
window.title("Encode / Decode app")
window.geometry("600x400+10+10")
window.resizable(False, False)
window.config(bg='#F1EBE4')

lbl_welcome = Label(window, text='Welcome to Decode / Encode app!', bg='#F1EBE4',font=('Arial',15,'bold'),
                    relief=RAISED, bd=1)
lbl_welcome.pack()
# btn = Button(window, text='start', bg='gray', fg='white', command=clicked)
# btn.grid(column=1, row=1)
# txt = Entry(window, width=10)
# txt.grid(column = 10, row=20)
# txt.focus()
window.mainloop()