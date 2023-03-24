import socket
import threading

# 서버의 IP 주소와 포트 번호를 지정합니다.
SERVER_HOST = '117.16.40.133'
SERVER_PORT = 8000

# 사용자 이름을 입력받습니다.
username = input("Enter your username: ")

# 서버에 연결합니다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 서버로 메시지를 전송하는 함수입니다.
def send_message():
    while True:
        message = input()
        if message == 'quit':
            # 사용자가 quit를 입력하면 소켓을 닫고 프로그램을 종료합니다.
            client_socket.close()
            break
        # 메시지를 서버로 전송합니다.
        client_socket.send(f"{username}: {message}".encode())

# 서버로부터 메시지를 수신하는 함수입니다.
def receive_message():
    while True:
        try:
            # 서버로부터 데이터를 수신합니다.
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # 예외가 발생하면 소켓을 닫고 프로그램을 종료합니다.
            client_socket.close()
            break

# 메시지를 전송하는 쓰레드와 메시지를 수신하는 쓰레드를 시작합니다.
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()
