from nibble import *
from http.server import HTTPServer, BaseHTTPRequestHandler

ed = pick_num()
print(ed)
result_ed = make_ed(ed)

braille_stack = []
for e in result_ed:
    s = encode_braille(change_braille(e))[2:]
    c = s.encode()
    braille_stack.append(c)

print(braille_stack)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plan')
        self.end_headers()
        self.wfile.write(b'bbbb:')
        for b in braille_stack:
            self.wfile.write(b)
            self.wfile.write(b":")

if __name__ =='__main__':
    server = HTTPServer(('', 8888), MyHandler)
    print('Started WebServer on port 8888…')
    print('Press ^c to quit webserver')
    server.serve_forever()
