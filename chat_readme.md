# cs372 - Chat Application using sockets

## Specification 
### REFERENCES
[Python DOCS](https://docs.python.org/3/library/socket.html#example)

### Server
1. the server creates a socket and binds to locahost and port 
2. server the listens for a connection
3. when a connections is made the server calls recv to receive data
4. the server prints the data then prompts for a reply
5. if the reply is /q, the server quits
6. otherwise, the server sends the reply
7. back to step 3
8. close the sockets 

### Client
1. the client creates a socket and connect to localhost and port 
2. when connected, the client prompts for a message to send 
3. if teh message is /q, the client quits
4. otherwise, teh client sends the message
5. the client calls recv to receive data
6. the client prints the data
7. back to step 2
8. close the sockets

Start the server:
  ```
  py chat_server.py <port> 
  ```
Then start the client:
  ```
  py chat_client.py <server port> 
  ```
