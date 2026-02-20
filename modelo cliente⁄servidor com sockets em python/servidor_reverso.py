import socket
import concurrent.futures

endereco_host = '' #porta ip, 0.0.0.0 escuta em todas as interfaces
porta = 5000                #porta
limite_fila = 5
tamanho_buffer = 1024

#função que trata cada cliente
def atender_cliente(conexao, endereco):
    print(f"[SERVIDOR] Conexão recebida de {endereco}")

    #receber dados do cliente
    dados = conexao.recv(tamanho_buffer).decode('utf-8')
    print(f"[SERVIDOR] Mensagem recebida: {dados}")

    # Reverter a string
    resposta = dados[::-1]

    # Enviar de volta
    conexao.sendall(resposta.encode('utf-8'))
    print(f"[SERVIDOR] Mensagem enviada: {resposta}")

    conexao.close()
    print(f"[SERVIDOR] Conexão encerrada com {endereco}")


def iniciar_servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((endereco_host, porta))
    servidor_socket.listen(limite_fila)

    print(f"[SERVIDOR] Servidor iniciado na porta {porta} e aguardando conexões...")

    # Pool de threads para limitar o número de atendimentos simultâneos
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        while True:
            conexao, endereco = servidor_socket.accept()
            pool.submit(atender_cliente, conexao, endereco)


if __name__ == "__main__":
    iniciar_servidor()
