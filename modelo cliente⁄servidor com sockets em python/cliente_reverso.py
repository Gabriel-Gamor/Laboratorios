import socket

endereco_servidor = ''   # IP do servidor
porta_servidor = 5000             #porta
tamanho_buffer = 1024

def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((endereco_servidor, porta_servidor))

    mensagem = "Olá Mundo Distribuído"
    print(f"[CLIENTE] Enviando: {mensagem}")

    cliente_socket.sendall(mensagem.encode('utf-8'))

    resposta = cliente_socket.recv(tamanho_buffer).decode('utf-8')
    print(f"[CLIENTE] Resposta do servidor: {resposta}")

    cliente_socket.close()


if __name__ == "__main__":
    iniciar_cliente()
