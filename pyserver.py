from http.server import HTTPServer, BaseHTTPRequestHandler

class ChunkedHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Transfer-Encoding', 'chunked')
        self.end_headers()

        for chunk in ['a' * 10, 'b' * 11, 'c' * 12]:
            self.wfile.write(b"%x\r\n%s\r\n" % (len(chunk), bytes(chunk, "utf8")))


HTTPServer(('', 8888), ChunkedHTTPRequestHandler).serve_forever()
