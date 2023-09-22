import http.server
import socketserver
from http import HTTPStatus

port = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_response(HTTPStatus.OK)
        super().end_headers()

    def do_GET(self):
        self.path = "response.json"
        return super().do_GET()

with socketserver.TCPServer(("", port), CustomHandler) as httpd:
    print(f"Server started on port {port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

# To test the server, you can access http://localhost:8080/ in your web browser.
