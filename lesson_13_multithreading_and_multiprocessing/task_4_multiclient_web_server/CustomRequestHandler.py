from http.server import SimpleHTTPRequestHandler


class CustomRequestHandler(SimpleHTTPRequestHandler):
    """
    Request Handler custom implementation
    """

    def do_GET(self) -> None:
        """
        Handle GET requests
        :return:
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, user!")
