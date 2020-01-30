from http.server import BaseHTTPRequestHandler, HTTPServer

x=0

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        x=x+1
        self.wfile.write(b"Hello, DB/PB, we are changing! Again!\n")
        self.wfile.write(x)
        return

httpd = HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()
