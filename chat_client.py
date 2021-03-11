import sys
import socket

HOST = 'localhost'
PORT = int(sys.argv[1])
buffer = 4096

if __name__ == "__main__":
  # 1. the client creates a socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as chat_client:
    try:
      # 1. connects to localhost and port
      chat_client.connect((HOST,PORT))
      client_msg = ''
      connected = 1
      while connected:
        # 2. when connected, the client prompts for a message to send
        client_msg = input("Enter message: ")
        # 3. if the messge is /q, the client quits
        if "/q" == client_msg:
          connected = 0
          break
        # 4. otherwise, the client sends the message
        chat_client.sendall(bytes(str(client_msg), encoding="utf-8"))
        # 5. the client calls recv to receive data
        server_res = chat_client.recv(buffer)
        if not server_res: 
          connected = 0
          chat_client.close()
          break
        if server_res.decode("utf-8") == "/q":
          connected = 0
          chat_client.close()
          break
        # 6. the client prints the data
        print("->SERVER: ", server_res.decode("utf-8")) 
        # 7. back to step 2
    except ConnectionAbortedError:
      print("SERVER DISCONNECTED")
      chat_client.close()
    # 8. sockets are closed, using with
    #chat_client.close()