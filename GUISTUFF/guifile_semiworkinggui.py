from Tkinter import *

def main(code):
    master = Tk()
    ret = []
    def return_entry(en):
        """Gets and prints the content of the entry"""
        content = entry.get()
        ret.append(content)
        master.destroy()
 
    Label(master, text="Input: ").grid(row=0, sticky=W)
    
    for i in range(len(code)):
        lit = Label(master, text=code[i], bg="white", fg="black").grid(row=i, column=0, sticky=W)
        #print(code[i])
        
#    but = Button(master, text="Insert Comment", command=return_entry)
#    but.pack(fill=X)


    entry = Entry(master)
    Label(master, text="Description: ", bg="red", fg="black").grid(column=0, sticky=W)
    entry.grid(column=0, sticky=W)

    strang = entry.get()

    # Connect the entry with the return button
    entry.bind('<Return>', return_entry)
    mainloop()
    #print("HERE: "+str(ret))
    return ret
    

    '''
    class MyFirstGUI:
        def __init__(self, master):
            self.master = master
            master.title("A simple GUI")

            for i in range(len(code)):
                self.label = Label(master, text=code[i], bg="white", fg="black")
                self.label.pack(anchor=W)

            self.e = Entry(root)
            self.e.pack()
            
            self.close_button = Button(master, text="Insert Comment", command=self.saveComment())
            self.close_button.pack(fill=X)
            
        def saveComment(self):
            print("HERE\n")
            print(self)
            print(self.e.get())
            #ret.append(e.get())
            print(ret)
            print("HERE2\n")
            self.master.quit()

    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
    return ret
    '''
