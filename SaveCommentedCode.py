def main(CommentedCode, OriginalName):
    #Strips '.cpp' off the file
    OriginalName = OriginalName[0:len(OriginalName)-4]
    
    #names new file with the '_commented.cpp' tag
    newfile = open(str(OriginalName)+"_commented.cpp",'w')

    for num in range(len(CommentedCode)):
        newfile.write(CommentedCode[num])
        newfile.write("\n")

    newfile.close()
