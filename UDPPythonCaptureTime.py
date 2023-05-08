from socket import *
import requests
import json

serverPort = 7000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    ClockRead, clientAddress = serverSocket.recvfrom(2048)
    print(ClockRead)
    ClockReadDecoded = ClockRead.decode()
    print("Received message:" + ClockReadDecoded)
    ClockRead={"Clock":f"{ClockReadDecoded}"}
    print(ClockRead)
    #ClockReadDe = json.loads(ClockRead)
    #print(ClockReadDe)

    
    api_url = "https://clockapi.azurewebsites.net/api/ClockReads"
    request = requests.post(api_url, json=ClockRead,verify=False)