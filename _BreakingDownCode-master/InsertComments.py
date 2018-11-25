#import guiFile

def main(TargerArray, Structure, function_location, function_list):
    #Node in C++
    #
    #  ///////////////////////////////////////////////////////
    #  //   Description of <function()>:
    #  //       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #  //   
    #  ///////////////////////////////////////////////////////
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
                #Use later when finishing GUI code
                #
                #code = []
                #for i in range(int(function_location[count]),int(function_location[count+1])):
                #    code.append(TargerArray[i])

                #Cats out the function that you are describing
                #
                print(" ________________________________________________________________")
                print("/ \                /                                             \ ")
                print("|  \  Function-"+str(funnum)+"  /                                              | ")
                print("|   \____________/                                               | ")
                print("|                                                                |")
                for i in range(int(function_location[count]),int(function_location[count+1])):
                    print("|	|"+str(TargerArray[i]))
                print("|                                                                |")
                print("\________________________________________________________________/\n")

                
                #Use later to insert newlines for descriptions over length 50 or so
                #
                #description = input("Description of "+str(function_list[count]+"():"))
                description = str(function_list[count])
                lines = (len(description)/50)+1
                InsertThis = []
                for num in range(int(lines)):
                    if(num==lines):
                        InsertThis.append(description[num*50:len(description)-1])
                    else:
                        InsertThis.append(description[num*50:(num+1)*50])

                #print("____\n")
                #print(lines)
                #print("____\n")

                #newArray.append("/*#------------------------------------------------------------|")
                newArray.append("/*#############################################################|")
                newArray.append("  # Function name: 	"+str(function_list[count])+"()")
                newArray.append("  # Input:		fill in later")
                newArray.append("  # Output:		fill in later")
                newArray.append("  # Description of ():	")
                #newArray.append("//#    "+str(input("Description of "+str(function_list[count]+"():"))))
                #newArray.append("  #	"+description)
                for here in range(len(InsertThis)):
                    newArray.append("  #	"+str(InsertThis[here]))

                newArray.append("  #############################################################|*/")
                #newArray.append("  #-----------------------------------------------------------*/")
                count = count+1
            #print(TargerArray[num])

    return newArray
    #print("_____")
