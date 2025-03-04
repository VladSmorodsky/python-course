import logging
import os
from http.server import ThreadingHTTPServer

from dotenv import load_dotenv

from CustomRequestHandler import CustomRequestHandler

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    server_host = os.getenv('SERVER_HOST', 'localhost')
    server_port = os.getenv('SERVER_PORT', '8080')
    server_address = (server_host, int(server_port))
    with ThreadingHTTPServer(server_address, CustomRequestHandler) as httpd:
        logging.info('Server started on port {}'.format(server_port))
        httpd.serve_forever()
except Exception as e:
    logging.error('Exception occurred: {}'.format(e))
