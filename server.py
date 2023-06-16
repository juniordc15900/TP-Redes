from header import header
from arquivo import retorna_arquivo
from ssocket import cria_socket

class Servidor:
    def __init__(self, host, porta, dir):
        self.host = host
        self.porta = porta
        self.dir = dir

    def start(self):
        #Instancia o socket
        server_socket = cria_socket(self.host,self.porta)
        print('Servidor iniciado')

        while True:
            # conexão cliente - servidor
            client_socket, client_address = server_socket.accept()
            request = client_socket.recv(1024).decode('utf-8')

            if request:
                request_method = request.split(' ')[0]
                request_path = request.split(' ')[1]

                if request_path == '/HEADER':
                    response = header(request)
                else:
                    response = retorna_arquivo(request_path,self.dir)

                # Envia a resposta ao cliente e fecha a conexão
                client_socket.sendall(response)
                client_socket.close()

