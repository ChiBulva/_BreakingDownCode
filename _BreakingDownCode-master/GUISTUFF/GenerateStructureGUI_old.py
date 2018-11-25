from Tkinter import *

def main(Structure, FunctionLocation, FindFunctionList):

    class MyStructureGUI:
        
    	def __init__(self, master):			
            Green = "Green"
            Yellow = "Yellow"
            Red = "Red"
			
            things_to_print=['something','one thing','another']

            for i in range(len(Structure)):
                    #if(Color!=Red):
                    #    self.label = Label(master, bg="White", fg="White", height=)
                    #    self.label.pack(fill=X)
                if("call" in str(Structure[i])):
                    Color = Red
                elif("For Loop" in str(Structure[i]) or "While Loop" in str(Structure[i]) or "If Statement" in str(Structure[i]) or "Switch Statement" in str(Structure[i]) or "Do while loop" in str(Structure[i])):
                    Color = Yellow
                else:
                    Color = Green

                self.label = Label(master, text=Structure[i], bg=Color, fg="black")
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
    my_gui = MyStructureGUI(root)
    root.mainloop()
    exit()

