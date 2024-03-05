import tkinter as tk
from tkinter import messagebox
import main


window = tk.Tk()
window.title('Menadżer Haseł')
window.config(padx=20, pady=20)

# ---------------- FUNKCJE ---------------- #

def dodajBut():

    if pasEnt.get() == '' or webEnt == '':
        messagebox.showinfo(title='Błąd', message='Zostawiłeś/aś wolne pole!')
    else:
        message = messagebox.askokcancel(title=f'{webEnt.get()}',
                                         message=f'Twoje informacje: \nEmail: {emaEnt.get()} \nHasło: {pasEnt.get()}'
                                                 f'\nCzy chcesz zapisać te informacje?')
        if message:
            with open('data.txt', 'a') as plik:
                plik.write(f'{webEnt.get()} | {emaEnt.get()} | {pasEnt.get()} \n')
                webEnt.delete(0, 'end')
                pasEnt.delete(0, 'end')


# ---------------- BUDOWA GUI -------------- #


canvas1 = tk.Canvas(width=200, height=200)
nazwa = tk.PhotoImage(file="logo.png")
canvas1.create_image(100, 100, image=nazwa)
canvas1.grid(row=0, column=1)

website = tk.Label(text='Strona:')
website.grid(row=1, column=0)

email = tk.Label(text='Email/Nazwa:')
email.grid(row=2, column=0)

haslo = tk.Label(text='Hasło:')
haslo.grid(row=3, column=0)

webEnt = tk.Entry(width=48)
webEnt.focus()
webEnt.grid(row=1, column=1, columnspan = 2)

emaEnt = tk.Entry(width=48)
emaEnt.grid(row=2, column=1, columnspan = 2)
emaEnt.insert(0, 'twójmail@gmail.com')

pasEnt = tk.Entry(width=33)
pasEnt.grid(row=3, column=1)

genPass = tk.Button(text='Generuj Hasło', command=main.hasloo)
genPass.grid(row=3, column= 2)

addButt = tk.Button(text='Dodaj', width=40, command=dodajBut)
addButt.grid(row=4, column=1, columnspan=2)


window.mainloop()