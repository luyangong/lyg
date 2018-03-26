from BaseHTTPRequestHandler import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_get(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'Welcom to the machine...'
        print 'Press ctrl+c once or twice to quit.'
        server.server_forever()
    except KeyboardInterrupt:
        print 'Ctrl+c received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
