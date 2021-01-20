# references
# https://docs.python.org/3/library/internet.html
# https://docs.python.org/3/library/http.server.html

import http.server
import http.client
import socketserver
import urllib.request
#gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n
PORT = 1234 
header_content = {}

### https://docs.python.org/3/howto/sockets.html
class MySocket:
  """demonstration class only
    - coded for clarity, not efficiency
  """

  def __init__(self, sock=None):
    if sock is None:
      self.sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    else:
      self.sock = sock

  def connect(self, host, port):
    self.sock.connect((host, port))

  def mysend(self, msg):
    totalsent = 0
    while totalsent < MSGLEN:
      sent = self.sock.send(msg[totalsent:])
      if sent == 0:
        raise RuntimeError("socket connection broken")
      totalsent = totalsent + sent

  def myreceive(self):
    chunks = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
      chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
      if chunk == b'':
        raise RuntimeError("socket connection broken")
      chunks.append(chunk)
      bytes_recd = bytes_recd + len(chunk)
    return b''.join(chunks)

ms = MySocket(address)
msc = ms.connect()
print(ms)

###

base_handler = http.server.BaseHTTPRequestHandler

# https://docs.python.org/3/library/socketserver.html
with socketserver.TCPServer(("", PORT), base_handler) as httpd:

  # https://docs.python.org/3/library/http.client.html#httpresponse-objects
  conn = http.client.HTTPConnection("gaia.cs.umass.edu")
  conn.request("GET", "/wireshark-labs/INTRO-wireshark-file1.html", )
  r1 = conn.getresponse()
  res_header = conn.getheader()
  print(res_header)
  while chunk := r1.read(200):
    print(repr(chunk))
  print("serving at port", PORT)
  httpd.serve_forever()