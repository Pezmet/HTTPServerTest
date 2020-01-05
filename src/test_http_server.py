import http.server
import simplejson


class Handler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_GET(self):
        self._set_headers()
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = simplejson.loads(data_string)
        print(f'{data}\n')
        self.end_headers()


def run(server_class=http.server.HTTPServer,
        handler_class=Handler,
        port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server Running at {httpd.server_address}')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
