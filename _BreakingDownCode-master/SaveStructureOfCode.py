def main(Structure, OriginalName):
    #Strips '.cpp' off the file
    OriginalName = OriginalName[0:len(OriginalName)-4]
    
    #names new file with the '_commented.cpp' tag
    newfile = open(str(OriginalName)+"_structure.cpp",'w')

    for num in range(len(Structure)):
        newfile.write(str(Structure[num]))
        newfile.write("\n")

    newfile.close()
