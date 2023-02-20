from socket import *
serverName = 'localhost'
serverPort = 12123

# create a socket, do NOT bind since not a server
clientSocket = socket(AF_INET, SOCK_DGRAM)

#  ask for input
message = input('Input lowercase sentence: ')

# send to the server
clientSocket.sendto(message.encode(), (serverName, serverPort))

# wait for the response
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print the reply
print(modifiedMessage)

# give back the resources
clientSocket.close()