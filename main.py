#Password Generator Project
import random
import gui
import pyperclip
def hasloo():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)


  literki = [random.choice(letters) for _ in range(nr_letters)]
  symbole = [random.choice(symbols) for _ in range(nr_symbols)]
  numery = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = literki + symbole + numery
  random.shuffle(password_list)

  password = "".join(password_list)
  gui.pasEnt.insert(0, password)
  pyperclip.copy(password)

  print(f"Your password is: {password}")