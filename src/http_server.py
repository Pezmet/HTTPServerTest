import http.server
import simplejson

from page.generate_html import DisplayPage
from notification.counter import NotificationCounter


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.data = None
        self.page = DisplayPage()
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.page.setBodyMessageNotificationCount(
            Context.count.notification_total)
        self.drawPage(self.page)

    def drawPage(self, page):
        self.wfile.write(page.startPageHtml())
        self.wfile.write(page.startPageHead())
        self.wfile.write(page.setPageTitle())
        self.wfile.write(page.endPageHead())
        self.wfile.write(page.setPageBody())
        self.wfile.write(page.endPageHtml())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.printNotificationAsJson()
        Context.count.filterNotificationByEvent(self.data)

    def printNotificationAsJson(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.data = simplejson.loads(data_string)
        if self.data is not None:
            print(f'{self.data}\n')
        else:
            raise print('Missing data in notification1!')


def run(server_class=http.server.HTTPServer,
        handler_class=Handler,
        port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server Running at {httpd.server_address}')
    Context.count = NotificationCounter()
    httpd.serve_forever()


def stop():
    print(' http server stopped...')
    quit()


class Context:
    count = None


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        try:
            run(port=int(argv[1]))
        except (KeyboardInterrupt, SystemExit):
            stop()
    else:
        try:
            run()
        except (KeyboardInterrupt, SystemExit):
            stop()
