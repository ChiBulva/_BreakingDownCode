import FindOrigninalName
import GenerateStructure
import TargetProgram
import StripStrings
import InsertComments
import SaveCommentedCode
import FindFunctionList
import FindFunctionLocation


StringsStripped = []
Structure = []
TargetArray = []
OriginalName = []
FunctionLocation = []
FunctionList = []

x = "Heellllloooooo!\n"
#Grabs a filename to comment out
OriginalName = FindOrigninalName.main()
#print(OriginalName)

#grabs entire program in plaintext and holds it in an array
TargetArray = TargetProgram.main(OriginalName)

#Strings the Program of all strings so you dont acccedentally count a character that shouldn't be counted
StringsStripped = StripStrings.main(TargetArray)

#Finds names of all functions
FunctionList = FindFunctionList.main(StringsStripped)

#Finds line number of every function
FunctionLocation = FindFunctionLocation.main(StringsStripped)

#for i in range(len(FunctionLocation)):
#    print(str(i+1)+": "+str(FunctionLocation[i]))
#    print(str(i+1)+": "+str(FunctionList[i]))


#Grabs function and create a structure of the program to reference points
Structure = GenerateStructure.main(StringsStripped, FunctionLocation, FunctionList)

#This section will eventually comment out your code
ComentedCode = InsertComments.main(TargetArray, Structure, FunctionLocation, FunctionList)

#This section will save the new code stored as 'ComentedCode'
#SaveCommentedCode.main(ComentedCode, OriginalName)

#Print statements from each function run
print("---STRIPPING---\n")
#for num in range(len(StringsStripped)):
#    print(StringsStripped[num])

print("---SEARCHING---\n")
print(" |_FindNames___\n")
print(" |_FindLocation\n")
#for num in range(len(TargetArray)):
#    print(TargetArray[num])

print("---STRUCTURE---\n")
for num in range(len(Structure)):
    print(Structure[num])

print("---COMMENTED---\n")
#for num in range(len(ComentedCode)):
#    print(ComentedCode[num])

print("--SAVING-CODE--\n")


print("---END--FILE---\n")
