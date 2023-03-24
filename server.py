import socket
import threading

# 서버의 IP 주소와 포트 번호를 지정합니다.
SERVER_HOST = '117.16.40.133'
SERVER_PORT = 8000

# 클라이언트의 연결을 처리하는 함수입니다.
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    while True:
        try:
            # 클라이언트로부터 데이터를 수신합니다.
            message = client_socket.recv(1024).decode()
            if message:
                print(f"[{client_address}]: {message}")
                # 모든 클라이언트에게 메시지를 전송합니다.
                broadcast_message(message, client_socket)
            else:
                # 클라이언트가 연결을 끊으면 반복문을 빠져나옵니다.
                break
        except:
            # 예외가 발생하면 클라이언트와의 연결을 끊습니다.
            client_socket.close()
            print(f"[DISCONNECTED] {client_address} disconnected.")
            break

# 모든 클라이언트에게 메시지를 전송하는 함수입니다.
def broadcast_message(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            client_socket.send(message.encode())

# 소켓 객체를 생성하고 연결을 바인딩합니다.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 클라이언트의 연결을 처리하는 쓰레드를 시작합니다.
def accept_clients():
    while True:
        # 클라이언트의 연결을 받습니다.
        client_socket, client_address = server_socket.accept()
        # 클라이언트를 리스트에 추가합니다.
        clients.append(client_socket)
        # 새로운 쓰레드를 시작해서 클라이언트의 연결을 처리합니다.
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# 클라이언트의 소켓 객체를 저장할 리스트를 생성합니다.
clients = []

# 서버를 시작합니다.
server_socket.listen()
print(f"[LISTENING] Server is listening on {SERVER_HOST}:{SERVER_PORT}")

# 클라이언트의 연결을 처리하는 쓰레드를 시작합니다.
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()
