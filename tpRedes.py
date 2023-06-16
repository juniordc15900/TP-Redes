from server import Servidor
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Simple HTTP Server')
    parser.add_argument('porta', type=int)
    parser.add_argument('directory')
    args = parser.parse_args()

    # Cria uma instância do servidor com base nos argumentos fornecidos
    server = Servidor('', args.porta, args.directory)
    
    # Inicia o servidor
    server.start()
