from Tkinter import *

def main(Structure, FunctionLocation, FindFunctionList, StringsStripped):

    class MyStructureGUI:
        
    	def __init__(self, master):			
            Green = "Green"
            Yellow = "Yellow"
            Red = "Red"
            Color = Green
			
            for i in range(len(Structure)):
                #FOUND FUNCTION
                if("\t" not in str(Structure[i])):
                    Color = Green
                #FOUND CALLs
                elif("call" in str(Structure[i])):
                    Color = Red
                #FOUND CONDITIONAL
                elif("For Loop" in str(Structure[i]) or "While Loop" in str(Structure[i]) or "If Statement" in str(Structure[i]) or "Switch Statement" in str(Structure[i]) or "Do while loop" in str(Structure[i]) or "else" in str(Structure[i])):
                    Color = Yellow
                #FOUND END OF CONDITION
                elif("\t" in str(Structure[i])):
                    Color = Yellow

                self.label = Label(master, text=Structure[i], bg=Color, fg="black")
                self.label.pack(anchor=W)
				
            self.master = master
            master.title("Structure of your code")

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack(fill=X)

        def greet(self):
            print("Greetings!")

    root = Tk()
    my_gui = MyStructureGUI(root)
    root.mainloop()
    exit()

