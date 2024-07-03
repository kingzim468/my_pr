from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 9998

class HandlerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(f"<h3>hello</h3>".encode('utf-8'))

service = HTTPServer(('', PORT), HandlerClass)
print('HTTP Server started...[', PORT, ']')
service.serve_forever()
