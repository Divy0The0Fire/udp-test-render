import socket

def udp_server():
    # Define the server address and port
    server_address = ("0.0.0.0", 5000)  # Listen on all interfaces

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address
    sock.bind(server_address)

    print(f"UDP server listening on {server_address}")

    while True:
        # Receive data from clients
        data, address = sock.recvfrom(1024)  # Buffer size of 1024 bytes
        print(f"Received {data} from {address}")

        # Send a response back to the client
        if data:
            response = b"Data received"
            sock.sendto(response, address)
print("sex")
if __name__ == "__main__":
    udp_server()
