from tkinter import *
from tkinter import messagebox
import random
import string

root = Tk()
root.geometry("900x900")
root.title("Password Generator")

def generatePassword():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%^&*()_-~?[]/"
    no_of_characters = int(user_input.get())
    passWord = ""
    for i in range(no_of_characters):
        random_choice = random.choice(characters)
        passWord += random_choice
    
    messagebox.showinfo("Password  Generator" ,f"Your password could be  {passWord}")

text_label = Label(root, text="Enter the total number of characters: ")
text_label.grid(row = 0, column = 0, padx = 10, pady = 20)


user_input = Entry(root)
user_input.grid(row = 0, column=1, padx = 10, pady = 20)

password_button = Button(root, text="Generate Password", command=generatePassword)
password_button.grid(row = 0, column=2, padx=10, pady=20)

root.mainloop()
