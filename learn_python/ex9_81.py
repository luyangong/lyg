import shutil, os, re

#os.mkdir('newtxt')
for *_, filenames in os.walk('.'):
    for file in filenames:
        if file[-4:] == '.txt':
            shutil.copy(file, 'newtxt')
        else:
            pass
