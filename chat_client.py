import sys
import socket

HOST = 'localhost'
PORT = int(sys.argv[1])
buffer = 4096

if __name__ == "__main__":
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as chat_client:
    chat_client.connect((HOST,PORT))
    client_msg = ''
    connected = 1
    while connected:
      client_msg = input("Enter message: ")
      if "/q" == client_msg:
        connected = 0
        break
      chat_client.sendall(bytes(str(client_msg), encoding="utf-8"))
      server_res = chat_client.recv(buffer)
      if "/q" == server_res.decode("utf-8"):
        connected = 0
        break
      print("->SERVER: ", server_res.decode("utf-8")) 
    chat_client.close()