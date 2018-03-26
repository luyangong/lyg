from urllib.request import urlopen


def get_page(url):
    def func(line):
        #bt = bytes(' \n\r', encoding='utf-8')
        line = line.strip(b' \n\r')
        if line:
            return True
        else:
            return False
    with urlopen(url) as f:
        data = f.readlines()
        line_withdata = list(filter(func, data))
        print(line_withdata[0].decode('utf-8'))
        print(line_withdata[-1].decode('utf-8'))

def main():
    url = input('Please input URL:\n')
    get_page(url)

if __name__ == '__main__':
    main()
