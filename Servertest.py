from socket import * 
serverPort = 5005
serverIP = "127.0.0.1"
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((serverIP,serverPort))
print("ready")
data,addr = serverSocket.recvfrom(1024)
print(f"recieve : {data.decode()}")
with open(data,"wb") as file:
    while True:
        data, _ = serverSocket.recvfrom(1024)
        if data == b"EOF":
            break
        file.write(data)

serverSocket.close()
