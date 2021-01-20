# cs372
## intro to networking

### Project 1 

* Make a socket connection to [host](gaia.cs.umass.edu)
* Send a GET request to the server:
  * '/wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
* Verify that the resource has been downloaded
* display the response at the home page of a local python server


####  To run the program and fetch the resource:

From the command line run:
1. Use python version >= 3. Haven't tested versions less than version 3
2. from the root project folder, run 
  ```
  python socket_server.py [your_specified port]
  ```
  or 
  ```
  py socket_server.py [your_specified port]
  ```
  or however your environment settings run python scripts.