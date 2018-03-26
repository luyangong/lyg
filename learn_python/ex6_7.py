def printTable(table):
    max_len = []
    raw = len(table)
    coloum = len(table[0])

    for i in range(raw):
        length = 0
        for j in range(coloum):
            if length < len(table[i][j]):
                length = len(table[i][j])
            else:
                pass
        max_len.append(length)

    for j in range(coloum):
        for i in range(raw):
            print(table[i][j].rjust(max_len[i]), end = ' ')
        print()

table = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]

printTable(table)
