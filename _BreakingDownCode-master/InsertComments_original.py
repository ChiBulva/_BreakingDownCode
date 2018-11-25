def main(TargerArray, Structure, function_location, function_list):
    # Number of new lines after this call is ran
    #    
    #    num of functions       number of lines for comment           new numbers of lines
    #
    #           x           *        5                          =          new number
    #
    
    
    #Node in C++
    #
    #  ///////////////////////////////////////////////////////
    #  //   Description of <function()>:
    #  //       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #  //   
    #  ///////////////////////////////////////////////////////

    #print("_____")

    newArray = []
    
    count = 0
    funnum = 0
    #adds length of the file so that I can cat out function as we go
    #
    function_location.append(len(TargerArray))
    

    for num in range(len(TargerArray)):
        newArray.append(TargerArray[num])
        if(count!=len(function_location)-1):        
            if(num+1==function_location[count]):
                funnum = funnum+1
                #Cats out the function that you are describing
                #
                print(" _______________________________________________________________")
                print("/ \                /                                            \ ")
                print("|  \  Function-"+str(funnum)+"  /                                              \ ")
                print("|   \____________/                                               | ")
                print("|                                                                |")
                for i in range(int(function_location[count]),int(function_location[count+1])):
                    print("|	|"+str(TargerArray[i]))
                print("\_____________________________________________________________/\n")

                
                #Use later to insert newlines for descriptions over length 50 or so
                #
                description = raw_input("Description of "+str(function_list[count]+"():"))
                lines = (len(description)/50)+1

                print(lines)

                newArray.append("//#------------------------------------------------------------|")
                newArray.append("//# Description of "+str(function_list[count])+"():")
                #newArray.append("//#    "+str(raw_input("Description of "+str(function_list[count]+"():"))))
                newArray.append("//#    "+description+"():")
                newArray.append("//#------------------------------------------------------------|")
                count = count+1
            #print(TargerArray[num])

    return newArray
    #print("_____")
