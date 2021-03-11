import socket
import sys

PORT = int(sys.argv[1])
HOST = 'localhost'
buffer = 4096

if __name__ == "__main__":
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as chat_server:
    # the microserver location that all other services will connect to
    chat_server.bind((HOST, PORT))
    # enable a server to accept connections
    chat_server.listen(5)
    connected = 1
    #while connected: # run the server until told to disconnect.
    (chat_client, addr) = chat_server.accept()
    with chat_client: 
      server_msg = '' 
      while connected:
        client_res = chat_client.recv(buffer)
        print("->CLIENT: ", client_res.decode("utf-8"))
        # prompt for a reply
        server_msg = input("Enter Message: ")
        if "\q" == server_msg:
          connected = 0
          chat_client.sendall(bytes(str(server_msg), encoding="utf-8"))
          break
        chat_client.sendall(bytes(str(server_msg), encoding="utf-8"))
      chat_client.close()
      chat_server.close()