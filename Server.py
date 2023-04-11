from socket import * 
import random   
serverPort=7000 
welcomingSocket = socket(AF_INET,SOCK_STREAM)
welcomingSocket.bind(('',serverPort)) 
serverName='Server of Group_7'
welcomingSocket.listen(1)
print('The server is ready to serve...')
while True:
   connectionSocket, client_address = welcomingSocket.accept()
   data_from_client= connectionSocket.recv(2048)     
   data_from_client = data_from_client.decode().split(',')  
   server_generated_integer= random.randint(1, 100)
   if not (1<= int(data_from_client[1])<=100):
       break
   sum_of_numbers = server_generated_integer + int(data_from_client[1])
   print("Client Name: ",data_from_client[0])   
   print("Integer input from client:", data_from_client[1])  
   print("Server generated number: ",server_generated_integer)
   print("Sum of numbers: ", sum_of_numbers)
   print("Client address: ",str(client_address)) 
   message_to_be_sent = serverName+"," + str(server_generated_integer)+","+str(sum_of_numbers)  
   connectionSocket.send(message_to_be_sent.encode())
   connectionSocket.close()

 
  
