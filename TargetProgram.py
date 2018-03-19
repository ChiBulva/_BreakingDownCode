import glob

def main(OriginalName):    
#    for filename in glob.glob('./FileSearched/*.cpp'):
#        #print(filename)
#        fh=open(filename)
#        lines = [line.rstrip() for line in fh.readlines()]
#        fh.close()


    #print(filename)
    fh=open(OriginalName)
    lines = [line.rstrip() for line in fh.readlines()]
    fh.close()
    
    #Indented = counter for how many open brackets you get.
    indented=0
    function_number=0
    
    return lines
