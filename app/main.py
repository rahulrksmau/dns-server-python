import socket

def main():
    # Initializing udp socket 
    udp_socket_init = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Binding to localhost
    udp_socket_init.bind(("127.0.0.1", 2053))
    while True:
        try:
            buf, source = udp_socket_init.recvfrom(512)
            response = b""
            udp_socket_init.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

if __name__ == "__main__":
    main()
