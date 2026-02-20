import socket
import threading
import datetime
import concurrent.futures

endereco_host = '' #ip, 0.0.0.0 escuta em todas as interfaces
porta = 5000 #porta de conexão
limite_fila = 5  #numero de conexões maximas pendentes
tamanho_buffer = 1024 #quantos bytes você lê ou envia por vez

#função atender cliente
def atender_cliente(conexao, endereco):
    print(f"[SERVIDOR] Conexão recebida de {endereco}")
    dados_recebidos = conexao.recv(tamanho_buffer) #dados enviados pelo cliente
    horario_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #pega hora
    conexao.sendall(horario_atual.encode('utf-8')) #Envia horário para o cliente
    print(f"[SERVIDOR] Horário enviado para {endereco}: {horario_atual}")
    conexao.close()  #fecha conexão com o cliente
def iniciar_servidor():
    #socket.AF_INET = endereços IPv4
    #socket.SOCK_STREAM = TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket TCP.
    servidor_socket.bind((endereco_host, porta)) #define IP e porta onde o servidor ficará.
    servidor_socket.listen(limite_fila) #coloca o servidor para escutar e define o tamanho da fila.
    print(f"Servidor iniciado e escutando em {endereco_host}:{porta}")

    '''
    while (True):
        conexao, endereco = servidor_socket.accept() #aceita uma nova conexão e cria um canal exclusivo para ela.
        # Criar uma thread para cada cliente
        thread_atendimento = threading.Thread(
            target=atender_cliente, #função que o thread vai rodar
            args=(conexao, endereco) #dados para essa função
        )
        thread_atendimento.start()
    #MEDO dado que vá aceitando podem gerar theads até o pc morrer
    '''
    
    #criar um pool de threads com limite fixo, mas o pc não morrer
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        while True:
            conexao, endereco = servidor_socket.accept()
            # Enviar a tarefa para o pool
            pool.submit(atender_cliente, conexao, endereco)

# Início do programa
if __name__ == "__main__":
    iniciar_servidor()
