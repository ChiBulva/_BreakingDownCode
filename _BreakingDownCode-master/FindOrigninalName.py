import glob

def main():    
    for filename in glob.glob('./FileSearched/*.cpp'):
        return filename
