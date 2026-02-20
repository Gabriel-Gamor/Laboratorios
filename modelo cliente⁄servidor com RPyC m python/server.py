import rpyc
from rpyc.utils.server import ThreadedServer #para varias vezes
from rpyc.utils.server import OneShotServer #para uma vez
from datetime import datetime


class TimeService(rpyc.Service):
    # Métodos expostos ao cliente devem começar com "exposed_"
    def exposed_get_time(self) -> str:
        # Retorna o horário atual no formato ISO
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    HOST = ""   # 0.0.0.0 escuta em todas as interfaces
    PORT = 18812 # porta padrão comum em exemplos RPyC
    
    # Se quiser fazer só responder uma unica vez
    print(f"[SERVIDOR] Rodando OneShot em {HOST}:{PORT}")
    OneShotServer(TimeService, hostname=HOST, port=PORT).start()
    print("[SERVIDOR] Pedido atendido.")
    print("[SERVIDOR] Servidor encerrando.")
    
    # ThreadedServer se quiser retornar varias requisições
    '''
    print(f"[SERVIDOR] Rodando em {HOST}:{PORT} ...")
    server = ThreadedServer(TimeService, hostname=HOST, port=PORT)
    server.start()
    '''