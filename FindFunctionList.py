import glob
    #TODO:  
    #	I need to scrub the .cpp file for strings and delete them
    #       

def main(TargetProgram):    
    #Indented = counter for how many open brackets you get.
    indented=0
    
    #This will end up being the array that will be returned as the function parser out.
    #
    function_list = []
    function_location = []
    
    for num in range(len(TargetProgram)):
        #This will search to see if you inside of a function or not. If you are
        #	This will look for function calls within the your current function.
        #       It will thn place them appropriately
        #       
        #Runs through each line of code
        #
        for i in TargetProgram[num]:
            #print("Here: "+str(i))
    
            if(i=='{'):
                #Checks to see if this is a base level function
                #
                indented=indented+1
                #Checks for if there was a function or not and labels it
                #
                if(indented==1):
                    start = 0
                    end = 0
                    number = 0
                    trigger = 0
                    funstr = []
                    placement = 0
                    
                    #checks for bracket on same line or not
                    if((len(TargetProgram[num]))==1):
                        placement = num-1
                    else:
                        placement = num
                    #placement = num
                    
                    #print("\n-->")
                    #print(TargetProgram[placement])
                    #print(len(TargetProgram[placement]))
                    #print((TargetProgram[placement][0]))
                    #print("<--\n")
                    #for char in TargetProgram[placement]:
                    #for char in TargetProgram[num]:
                    for char in TargetProgram[placement]:
                        number = number+1
                        if(char=='('):
                            end = number
    #                        newArray.append(str(number)+"<--end")
                            if(TargetProgram[placement][start:end-1]=="main"):
                                main_place = placement
                            
                            function_location.append(placement)
                            function_list.append(TargetProgram[placement][start:end-1])
                            funstr.append(char) 
                            break
                        if(char==' ' and trigger!=1):
                            start = number
                            trigger = 1
    
            if(i=='}'):
                indented=indented-1
                #Checks to see if this is a base level function
    #print("\n")
    #for i in range(len(function_location)):
    #    print(function_list[i])

    return function_list
