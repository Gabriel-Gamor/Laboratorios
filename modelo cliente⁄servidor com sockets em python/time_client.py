import socket

# Configurações do servidor
endereco_servidor = ''  # mesmo IP do servidor
porta_servidor = 5000              # mesma porta configurada no servidor
tamanho_buffer = 1024              # mesmo buffer do servidor

def solicitar_horario():
    # Cria o socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Tenta conectar ao servidor
        print(f"[CLIENTE] Conectando ao servidor em {endereco_servidor}:{porta_servidor}...")
        cliente_socket.connect((endereco_servidor, porta_servidor))

        # Envia uma string qualquer (o servidor nem usa, mas precisa enviar algo)
        mensagem = "SOLICITAR_HORARIO"
        cliente_socket.sendall(mensagem.encode('utf-8'))

        # Recebe o horário
        dados = cliente_socket.recv(tamanho_buffer)
        horario_recebido = dados.decode('utf-8')

        print(f"[CLIENTE] Horário recebido do servidor: {horario_recebido}")

    except Exception as erro:
        print(f"[CLIENTE] Erro ao comunicar com o servidor: {erro}")

    finally:
        cliente_socket.close()
        print("[CLIENTE] Conexão encerrada.")

# Início do programa
if __name__ == "__main__":
    solicitar_horario()
