#!/usr/bin/python3
"""Simple API built with the http.server module."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handles GET requests for a few simple endpoints."""

    def _send(self, code, body, content_type="text/plain"):
        """Sends a response with the given status, body and content type."""
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        """Routes GET requests to the matching endpoint."""
        if self.path == "/":
            self._send(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, json.dumps(data), "application/json")
        elif self.path == "/status":
            self._send(200, "OK")
        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self._send(200, json.dumps(info), "application/json")
        else:
            self._send(404, "Endpoint not found")


def run(port=8000):
    """Starts the HTTP server on the given port."""
    server = HTTPServer(("", port), SimpleAPIHandler)
    print("Serving on port {}".format(port))
    server.serve_forever()


if __name__ == "__main__":
    run()
