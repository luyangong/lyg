word = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
file_in = open('test.txt')
content = file_in.read()
file_in.close()
#print(content)
content_list = content.split()
#print(content_list)
content_out = []
for i in content_list:
        if i[0] in 'aA':
                ch = 'an'
        else:
                ch = 'a'
        if i in word:
                print('Enter ' + ch + ' ' + i + ':')
                i = input()
        elif i[:len(i) -1] in word:
                print('Enter ' + ch + ' ' + i[:len(i) - 1] + ':')
                i = i.replace(i[:len(i) - 1], input())
        else:
                pass
        content_out.append(i)
#print(content_out)
file_out = open('out.txt', 'w')
print(' '.join(content_out))
file_out.write(' '.join(content_out))
file_out.close()
