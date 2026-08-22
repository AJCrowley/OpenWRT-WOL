from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import subprocess

ETHERWAKE_CMD = "/usr/bin/etherwake"
INTERFACE = "br-lan"
PORT = 5050

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/wol":
            params = parse_qs(parsed.query)
            MAC = params.get("mac", [None])[0]

            if not MAC:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing MAC address")
                return

            subprocess.run(
                [ETHERWAKE_CMD, "-D", "-i", INTERFACE, MAC],
                check=True
            )

            dateFormatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"PC wake signal sent to {MAC} at {dateFormatted}"

            self.send_response(200)
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Server running on port {PORT}...")
server.serve_forever()
