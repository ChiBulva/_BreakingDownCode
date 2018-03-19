import glob
    #TODO:  
    #       
    #      Find the conditinal statements
    # 

def main(TargetProgram, function_location, function_list):    
    #Indented = counter for how many open brackets you get.
    indented=0
    
    #This will end up being the array that will be returned as the function parser out.
    #
    newArray = []
    
    for num in range(len(TargetProgram)):
        _open = "/"
        _close = "\ "
        #_open = "V"
        #_close = "^"
    
        #This will search to see if you inside of a function or not. If you are
        #	This will look for function calls within the your current function.
        #       It will thn place them appropriately
        #       
        if(indented>=1):
            for check in range(len(function_list)):
                if(str(function_list[check]+"(") in TargetProgram[num]):
                    #print(TargetProgram[num])
                    #call = str(function_list[check]+" "+str(function_location[check]))
                    call = str(function_list[check])
                    #for char in range(indented-1):
                    for char in range(indented):
                        call = "	"+call
 
                    newArray.append(call+" <-- function call")
    
        #Runs through each line of code
        #
        for i in TargetProgram[num]:
    
            if(i=='{'):
                #Checks to see if this is a base level function
                #
                if(indented>0):
                    for ind in range(indented):
                        _open = "	"+_open
    
                indented=indented+1
                newArray.append(_open)
                #Checks for if there was a function or not and labels it
                #
                if(indented==1):

                    number = 0		#counter that will assign start and end of function name
                    trigger = 0		#Will kee track of if the first space has been hit or not
                    placement = 0	#This is a toggle to cover both bracket on line and next line styles
                    
                    #Checks for bracket on same line or not and sets the placement variable
                    #
                    if((len(TargetProgram[num]))==1):
                        placement = num-1
                    else:
                        placement = num

                    #Takes a line that meets conditions such as bracket location and parses for function name
                    #
                    for char in TargetProgram[placement]:
                        number = number+1
                        if(char=='('):

                            end = number	#End is set the space where the "(" is found

                            #Stroers where the main function is located
                            #
                            if(TargetProgram[placement][start:end-1]=="main"):
                                main_place = placement
                            
                            #if uncommented, will store with line number 
                            #newArray.append(str(TargetProgram[placement][start:end-1])+" "+str(placement))
                            newArray.append(str(TargetProgram[placement][start:end-1]))

                            #Print statement for error checking
                            #
                            #print("Start: "+str(start)+" |End: "+str(end)+"  |Function name: "+str(TargetProgram[placement][start:end-1]))
                            break
                            
                        if(char==' ' and trigger!=1):
                            start = number
                            trigger = 1
            #This will find the end of a function or condition and save it then ittorate the indented flag
            #
            if(i=='}'):
                indented=indented-1
                #Checks to see if this is a base level function. If not, braces are used for a conditional
                #
                if(indented>0):
                    for ind in range(indented):
                        _close = "	"+_close
                #Saves a closing slash
                newArray.append(_close)
    
    #Places a map to link source code with structure
    #
    for num in range(len(function_location)):
        newArray.append(function_location[num])

     #Print Statement for debugging
#    for num in range(len(function_list)):
#        print(str(function_list[num])+" "+str(function_location[num]))
        

    return newArray
