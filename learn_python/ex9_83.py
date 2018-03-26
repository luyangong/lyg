import shutil, os, re

dataPattern = re.compile(r'''
    ([a-z]+)
    (\d+)
    ''', re.VERBOSE)
print('Please input the prefix:', end='')
prefix = input()
filenumber = {}

for filename in os.listdir():
    if os.path.isfile(filename) and filename.endswith('.txt'):
        rgx = dataPattern.search(filename)
        if rgx.group(1) == prefix:
            filenum[filename] = int(rgx.group(2))
        else:
            pass
    else:
        pass

for file, num in filenum.items():
    
                
