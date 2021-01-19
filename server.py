# references
# https://docs.python.org/3/library/http.server.html
import http.server
import socketserver

PORT = 1234 

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
  print("serving at port", PORT)
  httpd.serve_forever()