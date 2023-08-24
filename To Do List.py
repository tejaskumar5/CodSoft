from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do List App',
                           font='Arial, 25 bold', width=10, bd=5, bg='lawngreen', fg='blue')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='Arial, 18 bold', width=10, bd=5, bg='lawngreen', fg='blue')
        self.label2.place(x=10, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='Arial, 18 bold', width=10, bd=5, bg='lawngreen', fg='blue')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial, 10 bold')
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font='Arial, 20 bold italic',
                             width=5, bd=5, bg='tan', fg='green', command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='Arial, 20 bold italic',
                              width=12, bd=5, bg='tan', fg='red', command=self.delete)
        self.button2.place(x=30, y=280)

        self.button3 = Button(self.root, text="Update", font='Arial, 20 bold italic',
                              width=5, bd=5, bg='tan', fg='indigo', command=self.update)
        self.button3.place(x=150, y=180)

        self.load_tasks()

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        self.save_tasks()
        self.text.delete(1.0, END)

    def delete(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            self.main_text.delete(selected_index)
            self.save_tasks()

    def update(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            updated_content = self.text.get(1.0, END)
            self.main_text.delete(selected_index)
            self.main_text.insert(selected_index, updated_content)
            self.save_tasks()
            self.text.delete(1.0, END)

    def save_tasks(self):
        with open('data.txt', 'w') as file:
            for index in range(self.main_text.size()):
                content = self.main_text.get(index)
                file.write(content)
        file.close()

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(END, line)
        except FileNotFoundError:
            pass

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()