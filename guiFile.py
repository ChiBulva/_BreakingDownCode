from Tkinter import *

def main(code):

    class MyFirstGUI:
        def __init__(self, master):

            things_to_print=['something','one thing','another']

            for i in range(len(code)):
                self.label = Label(master, text=code[i], bg="white", fg="black")
                self.label.pack(anchor=W)
            
            self.master = master
            master.title("A simple GUI")

            self.greet_button = Button(master, text="Description", command=self.greet, background="red")
            self.greet_button.pack(fill=X)

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack(fill=X)

        def greet(self):
            print("Greetings!")

    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

