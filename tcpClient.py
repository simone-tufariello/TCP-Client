import socket

# tcp client basilare, senza controlli sui dati ricevuti

target_host = "www.google.com"
target_port = "80"

# creiamo un oggetto socket
# SOCK_STREAM = usiamo indirizzo IPv4
# AF_INET = creiamo una socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connettiamo il client
client.connect((target_host, target_port))

# inviamo dei dati 
client.send(b"GET / HTTP/1.1 \r\n Host: google.com \r\n\r\n")

# riceviamo risposta
response = client.recv(4096)
print(response.decode)
client.close()