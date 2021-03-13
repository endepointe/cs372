import socket
import sys

PORT = int(sys.argv[1])
HOST = 'localhost'
buffer = 4096

if __name__ == "__main__":
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as chat_server:
    try:
      # 1. The server creates a socket and binds to localhost and port
      chat_server.bind((HOST, PORT))
      # 2. the server listens for a connection
      chat_server.listen(5)
      connected = True
      # 3. when connected, the server calls recv to receive data
      (chat_client, addr) = chat_server.accept()
      #with chat_client: 
      server_msg = '' 
      while connected:
        # 3. continued
        client_res = chat_client.recv(buffer)
        if not client_res: 
          connected = False
          break
        # 4. the server prints the data
        print("->CLIENT: ", client_res.decode("utf-8"))
        # 4. the prompts for a reply
        server_msg = input("Enter Message: ")
        # 5. if the reply is /q, the server quits
        if "\q" == server_msg:
          connected = False
          break
        # 6 otherwise, the server sends the reply
        chat_client.sendall(bytes(str(server_msg), encoding="utf-8"))
        # 7 back to step 3 
    except ConnectionAbortedError:
      print("CLIENT DISCONNECTED")
      chat_client.close()
  # 8. sockets are closed, using with
  chat_server.close()
