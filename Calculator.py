from tkinter import *
import math

def button_press(num):
     global equation_text
     equation_text = equation_text + str(num)
     equation_label.set(equation_text)

def equals():
    global equation_text
    try:
      total = str(eval(equation_text))
      equation_label.set(total)
      equation_text = total
    except BaseException as be:
        equation_label.set("Error!")
        

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x500")
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()


frame = Frame(window)
frame.pack()

b1 = Button(frame, text=1, height=2, width=5, font=35, command= lambda: button_press('1'))
b1.grid(row=0,column=0)

b2 = Button(frame, text=2, height=2, width=5, font=35, command= lambda: button_press('2'))
b2.grid(row=0,column=1)

b3 = Button(frame, text=3, height=2, width=5, font=35, command= lambda: button_press('3'))
b3.grid(row=0,column=2)

b4 = Button(frame, text=4, height=2, width=5, font=35, command= lambda: button_press('4'))
b4.grid(row=1,column=0)

b5 = Button(frame, text=5, height=2, width=5, font=35, command= lambda: button_press('5'))
b5.grid(row=1,column=1)

b6 = Button(frame, text=6, height=2, width=5, font=35, command= lambda: button_press('6'))
b6.grid(row=1,column=2)

b7 = Button(frame, text=7, height=2, width=5, font=35, command= lambda: button_press('7'))
b7.grid(row=2,column=0)

b8 = Button(frame, text=8, height=2, width=5, font=35, command= lambda: button_press('8'))
b8.grid(row=2,column=1)

b9 = Button(frame, text=9, height=2, width=5, font=35, command= lambda: button_press('9'))
b9.grid(row=2,column=2)

b0 = Button(frame, text=0, height=2, width=5, font=35, command= lambda: button_press('0'))
b0.grid(row=3,column=1)

clear_button = Button(frame, text='=', height=2, width=5, font=40, command= lambda: equals())
clear_button.grid(row=3,column=2)

dot_button = Button(frame, text='.', height=2, width=5, font=88, command= lambda: button_press('.'))
dot_button.grid(row=3,column=0)

plus = Button(frame, text="+", height=2, width=5, font=35, command= lambda: button_press('+'))
plus.grid(row=0,column=3)

minus = Button(frame, text="-", height=2, width=5, font=35, command= lambda: button_press('-'))
minus.grid(row=1,column=3)

multiply = Button(frame, text="*", height=2, width=5, font=35, command= lambda: button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(frame, text="/", height=2, width=5, font=35, command= lambda: button_press('/'))
divide.grid(row=3,column=3)

S = Button(window, text="Clear", height=2, width=23, font=35, command= lambda: clear())
S.pack()

window.mainloop()

