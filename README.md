# Chat_Room_Application

> **Problem Statement:**
You have to develop a simple Chat Room server and allow multiple clients to connect to it using a client-side script. For this you have to set up a socket on each end and allow the client to interact with other clients via server. Any client that has the socket associated with the same port can communicate with that server socket. To handle multiple clients Multi-Threading is required. Every time a user connects to the server, a separate thread is created for that user and communication from server to client takes place through that individual thread.

> **Server Side Script:**
The server side script will attempt to 
> *	Establish a socket
> *	Bind it to an IP address and port specified 
> *	Start listening
> *	Receive connection requests
> *	Keep track of active connections (for multi-client chat)
> *	For each new user:
>   *	Create a separate thread 
>   *	Server awaits a message, and sends that message to other users currently on the chat. 
>   *	If server do not receive a message while trying to receive a message from a particular thread, it will exit that thread.
