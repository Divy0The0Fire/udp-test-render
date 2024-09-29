import socket

def udp_server():
    # Define server address and port
    server_address = ("0.0.0.0", 5000)  # '0.0.0.0' allows all network interfaces
    
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the server address
    sock.bind(server_address)
    
    print(f"Server listening on {server_address}")

    while True:
        data, address = sock.recvfrom(1024)  # Receive 1024 bytes from client
        print(f"Received {data} from {address}")
        
        # Send response back to the client
        if data:
            response = b"Data received"
            sock.sendto(response, address)

if __name__ == "__main__":
    udp_server()
