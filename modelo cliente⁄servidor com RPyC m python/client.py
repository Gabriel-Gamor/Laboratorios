import rpyc

if __name__ == "__main__":
    SERVER_IP = ""  # IP do servidor na rede
    PORT = 18812  # porta padrão comum em exemplos RPyC

    # Conecta, chama o método remoto e encerra
    conn = rpyc.connect(SERVER_IP, PORT)
    try:
        horario = conn.root.get_time()
        print(f"[CLIENTE] Horário do servidor: {horario}")
    finally:
        conn.close()
