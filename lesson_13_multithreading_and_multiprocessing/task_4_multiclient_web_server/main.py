import os
from http.server import ThreadingHTTPServer

from dotenv import load_dotenv

from CustomRequestHandler import CustomRequestHandler

load_dotenv()

try:
    server_host = os.getenv('SERVER_HOST', 'localhost')
    server_port = os.getenv('SERVER_PORT', '8080')
    server_address = (server_host, int(server_port))
    with ThreadingHTTPServer(server_address, CustomRequestHandler) as httpd:
        print('Server started on port {}'.format(server_port))
        httpd.serve_forever()
except Exception as e:
    print(e)
