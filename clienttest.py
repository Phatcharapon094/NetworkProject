from socket import * 
serverName = '127.0.0.1'
serverPort = 5005
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = "Thisisfile"
clientSocket.sendto(sentence.encode(), (serverName,serverPort))
print(f'sent {sentence}')
