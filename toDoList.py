from tkinter import *
from tkinter import messagebox

# for adding new task
def newTask():
    task = user_entry.get()
    if task in task_list:
        messagebox.showwarning("Warning", "The task already exist!")
    if task != "":
        lb.insert(END, task)
        user_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")


# for deleting selected task
def deleteTask():
    lb.delete(ANCHOR)


# Creating MainWindow
work_space = Tk()
work_space.geometry('500x500')
work_space.title('TO - DO List')
work_space.config(bg='#223441')
work_space.resizable(width=False, height=False)

# out Comes
frame = Frame(work_space)
frame.pack(pady=10)

# list box
lb = Listbox(
    frame,
    width=45,
    height=15,
    font=('Times', 10),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"
)

lb.pack(side=LEFT, fill=BOTH)

task_list = ['Add your Task']

for item in task_list:
    lb.insert(END, item)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=lb.yview)

user_entry = Entry(
    work_space,
    font=('Times',22)
)


user_entry.pack(pady=25)

button_frame = Frame(work_space)
button_frame.pack(pady=25)

# Task Add Button
addTask_button = Button(
    button_frame,
    text = 'Add Task',
    font = ('Times 14'),
    bg = '#c5f776',
    padx=20,
    pady=10,
    command = newTask
)
addTask_button.pack(fill=BOTH, expand=True, side=LEFT)

# Delete Button
deleteTask_button = Button(
    button_frame,
    text = "Delete Task",
    font = ('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)

deleteTask_button.pack(fill=BOTH, expand=True, side=RIGHT)


# Clossing
work_space.mainloop()