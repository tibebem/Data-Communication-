from socket import *
serverPort = ("127.0.0.1",7000) 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverPort)
clientName='Client of Group_7'
inputNumber=int(input('Please enter a number within the range [1,100]'))
message_to_be_sent = clientName+","+ str(inputNumber)
clientSocket.send(message_to_be_sent.encode()) 
data_from_server = clientSocket.recv(2048)
data_from_server = data_from_server.decode().split(',') 
print("Server Name: " , data_from_server[0]) 
print("Server generated number: " ,data_from_server[1])
print("Sum of numbers: " ,data_from_server[2])
clientSocket.close()
