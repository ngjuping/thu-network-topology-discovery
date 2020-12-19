import http.server
import socketserver
import signal
import sys

def signal_handler(sig, frame):
    print('Server closed')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.js'] = 'application/javascript'

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port: ", PORT)
    httpd.serve_forever()