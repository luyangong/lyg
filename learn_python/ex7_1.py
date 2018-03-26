import re
from sys import exit

def is_password():
    
    rex1 = re.compile(r'[A-Z]+')
    rex2 = re.compile(r'[a-z]+')
    rex3 = re.compile(r'\d+')

    print('Please input your password:', end = '')
    password = input('  ')

    if len(password) > 7:
        pass
        if rex1.search(password) != None:
            pass
            if rex2.search(password) != None:
                pass
                if rex3.search(password) != None:
                    print('It is a good password. Congratulations!')
                else:
                    print('One or more number should be contained in your password.')
                    exit()
            else:
                print('One or more character in lower case should be contained.')
                exit()
        else:
            print('One or more character in upper case should be contained.')
            exit()
    else:
        print('The length of your password should not less than eight.')

is_password()
