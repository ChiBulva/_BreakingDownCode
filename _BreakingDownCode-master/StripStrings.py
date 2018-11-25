def main(TargetProgram):    
    #Indented = counter for how many open brackets you get.
    indented=0
    
    #This will end up being the array that will be returned as the function parser out.
    #
    newArray = []
    function_list = []
    function_location = []
    
    trigger = 0
    string = []
    
    for num in range(len(TargetProgram)):
        _open = "/"
        _close = "\ "
        string[:] = []
        #Runs through each line of code
        #
        for i in range(len(TargetProgram[num])):
            if(trigger>=1):
                trigger = trigger+1
            if(TargetProgram[num][i]=='"' and trigger==0):
                trigger = 1
            if(TargetProgram[num][i]=='"' and trigger>1):
                trigger = 0
            if(trigger>1):
                string.append("*")
            else:
                string.append(TargetProgram[num][i])
                
        #newArray.append(TargetProgram[num])
        newArray.append(''.join(string))
        #print(newArray[num])
        
    return newArray
