import os, re

regex = re.compile(r'[tT]he')

for filename in os.listdir('.'):
        if filename.endswith('.txt'):
                File = open(filename)
                content = File.readlines()
                File.close()
                for sentence in content:
                        if regex.search(sentence):
                                print(sentence)
                        else:
                                pass
        else:
                pass
