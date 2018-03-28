from Tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
    frame.pack()
    for i in range(5):
        for j in range(5):
            if(j==4):
                print"hello"
            else:
                self.frm = Frame(frame, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
                self.frm.grid(row=i,column=j)
				
                self.button1 = Button(self.frm, text="QUIT1").grid(row=0,column=0)
                #self.button1.pack(side=LEFT)

                self.button2 = Label(self.frm, text="QUIT2", fg="red").grid(row=1,column=0)
                #self.button2.pack(side=LEFT)

                self.button3 = Label(self.frm, text="QUIT3", fg="red").grid(row=0,column=1)
                #self.button3.pack(side=LEFT)

                self.button4 = Label(self.frm, text="QUIT4", fg="red").grid(row=1,column=1)
                #self.button4.pack(side=LEFT)
				
				
                #self.button.pack()
  def write_slogan(self):
    print "Tkinter is easy to use!"

root = Tk()
app = App(root)
root.mainloop()