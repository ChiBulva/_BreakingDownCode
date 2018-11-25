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
        
                    #This will find how many variables per function call
                    #
#                    variables = 0
#                    if("," in TargetProgram[num]):
#                        variables = 1
#                        for i in range(len(TargetProgram[num])):
#                            if(TargetProgram[num][i]==','):
#                               variables = variables+1
                    
        
#                    print("Variables: "+str(variables)+"\n")
                    for char in range(indented):
                        call = "	"+call
        
#                    newArray.append(call+" <-- function call with "+str(variables)+" variables!")
                    newArray.append(call+" <-- function call")
            
            if("for" in TargetProgram[num] and "(" in TargetProgram[num]):
                call = "For Loop"
                for char in range(indented):
                    call = "	"+call
                newArray.append(call)
            elif("while" in TargetProgram[num] and "(" in TargetProgram[num]):
                call = "While Loop"
                for char in range(indented):
                    call = "	"+call
                newArray.append(call)
            elif("if" in TargetProgram[num] and "(" in TargetProgram[num]):
                call = "If Statement"
                for char in range(indented):
                    call = "	"+call
                newArray.append(call)
            elif("switch" in TargetProgram[num] and "(" in TargetProgram[num]):
                call = "Switch Statement"
                for char in range(indented):
                    call = "	"+call
                newArray.append(call)
            elif("do" in TargetProgram[num] and "{" in TargetProgram[num]):
                call = "Do while loop"
                for char in range(indented):
                    call = "	"+call
                newArray.append(call)
            
        #Runs through each line of code
        #
        for i in TargetProgram[num]:
            #print(TargetProgram[num])
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
                    start = 0
                    #Checks for bracket on same line or not and sets the placement variable
                    #
                    if((len(TargetProgram[num]))==1):
                        placement = num-1
                    else:
                        placement = num
                    
                    #Takes a line that meets conditions such as bracket location and parses for function name
                    #
                    #for char in TargetProgram[placement]:
                    for char in range(len(TargetProgram[placement])):
                        number = number+1
                        if(TargetProgram[placement][char]=='('):
                            
                            end = number	#End is set the space where the "(" is found
                            
                            #Finds how many variables (add logic later to name them)
                            #
                            variables = 0
                            if(TargetProgram[placement][char+1]!=')'):
                                #Start of a variable
                                #
                                varStr = end
                                #Will eventually hold all of the variables being passed into a function
                                #
                                variablesList = []
#                                print("HERE: ")
                                for i in range(len(TargetProgram[placement])):
                                    if(TargetProgram[placement][i]==',' or TargetProgram[placement][i]==')'):
                                        varEnd = i
                                        variablesList.append(TargetProgram[placement][varStr:varEnd])
                                        variables = variables+1
#                                        print(str(TargetProgram[placement][varStr:varEnd])+" | ")
                                        varStr = varEnd+1
                                        
                            result = TargetProgram[placement][start:end-1]
                            #print("{-->"+result)
                            for r in range(variables):
                                if(r==0):
                                    result = str(result+" -> |Var #"+str(r+1)+": '"+variablesList[r]+"'")
                                else:
                                    result = str(result+" |Var #"+str(r+1)+": '"+variablesList[r]+"'")
                            #Stroers where the main function is located
                            #
                            if(TargetProgram[placement][start:end-1]=="main"):
                                main_place = placement
                            
                            #if uncommented, will store with line number 
                            
#  Places name of funC+line  #newArray.append(str(TargetProgram[placement][start:end-1])+" "+str(placement))
# Just places name of func   newArray.append(str(TargetProgram[placement][start:end-1]))
#                            newArray.append(str(TargetProgram[placement][start:end-1])+" with -> "+str(variables)+" variables")
                            newArray.append(result)
                            
                        
                            break
                            
                        if(TargetProgram[placement][char]==' ' and trigger!=1):
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
