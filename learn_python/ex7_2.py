import re

def mystrip(par1, par2 = ''):

    if len(par2) == 0:

        white_space = re.compile(r'(^\s+)|(\s+$)')

        print(white_space.sub('', par1))
    else:
        word = list(par1)
        while True:
            if word[0] in par2:
                del word[0]
            elif word[-1] in par2:
                del word[-1]
            else:
                break
        print(''.join(word))

mystrip('  hell0 ')

mystrip('or d helloworldooor', ' or')
        
        
        
