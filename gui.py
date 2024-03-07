import tkinter as tk
from tkinter import messagebox
import main
import json


window = tk.Tk()
window.title('Menadżer Haseł')
window.config(padx=20, pady=20)

# ---------------- FUNKCJE ---------------- #

def dodajBut():

    strona = webEnt.get()
    mail = emaEnt.get()
    password = pasEnt.get()
    dataaa = {
        strona: {
        'email': mail,
        'password': password
        }
    }
    if pasEnt.get() == '' or webEnt == '':
        messagebox.showinfo(title='Błąd', message='Zostawiłeś/aś wolne pole!')
    else:
        try:
            with open('data.json', 'r') as plik:

                dataa = json.load(plik)
                dataa.update(dataaa)

        except FileNotFoundError:
            with open('data.json', 'w') as plik:
                json.dump(dataaa, plik, indent=4)

        else:
            with open('data.json', 'w') as plik:

                json.dump(dataa, plik, indent=4)

        finally:
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

webEnt = tk.Entry(width=33)
webEnt.focus()
webEnt.grid(row=1, column=1)

emaEnt = tk.Entry(width=48)
emaEnt.grid(row=2, column=1, columnspan = 2)
emaEnt.insert(0, 'twojmail@gmail.com')

pasEnt = tk.Entry(width=33)
pasEnt.grid(row=3, column=1)

genPass = tk.Button(text='Generuj Hasło', command=main.hasloo)
genPass.grid(row=3, column= 2)

search = tk.Button(text='Szukaj', width=11)
search.grid(row=1, column=2)

addButt = tk.Button(text='Dodaj', width=40, command=dodajBut)
addButt.grid(row=4, column=1, columnspan=2)


window.mainloop()