from urllib.request import urlretrieve
from urllib.parse import urlparse
import os, sys
import http

class Retriever(object):
    __slots__ = ('url', 'file')
    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        'get a filename for saving the data from the url'
        parsed = urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        prot = parsed.scheme
        filepath = '%s%s' % (host, parsed.path)
        if not os.path.splitext(parsed.path)[-1]:
            if prot == 'http':
                filepath = os.path.join(filepath, default)
        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        try:
            retval = urlretrieve(self.url, self.file)
        except (IOError, http.client.InvalidURL) as e:
            retval = (('***Error! bad URL "%s": "%s"' % (self.url, e)), )
        return retval

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = input('Enter your URL:\n')
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url:
        return
    if not url.startswith('http://') and not url.startswith('ftp://'):
        if ':' not in url:
            url = 'http://' + url
        else:
            print('Your protocal may be wrong! Quit...')
            return
    ret = Retriever(url)
    filepath = ret.download()[0]
    print('The file has been saved in %s' % filepath)

if __name__ == '__main__':
    main()
