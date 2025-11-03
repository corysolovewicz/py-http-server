import http.server, socketserver, os

PORT, DIRECTORY = 8000, "files"
os.makedirs(DIRECTORY, exist_ok=True)

handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(*a, directory=DIRECTORY, **kw)
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving '{DIRECTORY}' at http://localhost:{PORT}")
    httpd.serve_forever()
