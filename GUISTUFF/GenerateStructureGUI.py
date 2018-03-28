from Tkinter import *

def main(Structure, FunctionLocation, FunctionList, StringsStripped):
    master = Tk()
    frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
    frame.pack()
    for functionNum in range(len(FunctionLocation)):
        print(FunctionList[functionNum])
    
    for i in range(len(FunctionLocation)-1):
        print(StringsStripped[int(FunctionLocation[i]):int(FunctionLocation[i+1])])
        lit = Label(frame, text=StringsStripped[int(FunctionLocation[i]):int(FunctionLocation[i+1])], bg="white", fg="black").grid(row=i, column=0, sticky=W)