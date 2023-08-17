from time import sleep
from http.server import HTTPServer,BaseHTTPRequestHandler

HOST = '0.0.0.0'

PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        message = "Hello World!"
        self.wfile.write(bytes(message, 'utf-8'))

def run(host, port, server_class=HTTPServer, hanlder_class=Handler):
    server_address = (host, port)
    httpd = server_class(server_address, hanlder_class)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    sleep(30)
    print("Starting server.....")
    run(HOST, PORT)