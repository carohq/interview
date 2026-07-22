import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from database import Database

db = Database()


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Add new routes here.
        if self.path == '/api/hello':
            self._send_json({'message': 'Hello from Python!'})
        else:
            self._send_json({'error': 'Not found'}, status=404)

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    server = ThreadingHTTPServer(('0.0.0.0', port), RequestHandler)
    print(f'Server is running on port {port}')
    server.serve_forever()
