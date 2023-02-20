from socket import *
serverPort = 12123

# serverSocket = a data structure - socket
serverSocket = socket(AF_INET, SOCK_DGRAM) # UDP socket, API to the OS

# start listening on this port
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

# infinite loop, keep checking for msgs
while 1:
	# call the recvFrom function, blocking call
	message, clientAddress = serverSocket.recvfrom(2048)
	# get the contents of the message, convert it to upper
	modifiedMessage = message.upper()
	# reply using the same socket, call sendto() function
	serverSocket.sendto(modifiedMessage, clientAddress)