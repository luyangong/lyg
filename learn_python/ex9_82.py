import os

print('Please input your direction:')
direction = os.path.abspath(input('> '))
size = {}

for foldername, subfolders, filenames in os.walk(direction, topdown=False):
    size[foldername] = 0
    for file in filenames:
        file = os.path.join(foldername, file)
        if  os.path.getsize(file):
            if os.path.getsize(file) >= 10000:
                print(file)
            else:
                pass
            size[foldername] += os.path.getsize(file)
        else:
            pass
    for subfolder in subfolders:
        subfolder = os.path.join(foldername, subfolder)
        size[foldername] += size[subfolder]
    if size[foldername] > 1000000:
        print(foldername)
        print('The size is %s'% size[foldername])
    else:
        pass
		
