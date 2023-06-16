import socket

def cria_socket(host,porta):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Associa o socket do servidor ao endereço e porta fornecidos
    s_socket.bind((host, porta))
    
    # Inicia a escuta do socket do servidor
    s_socket.listen(1)
    return s_socket