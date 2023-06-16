import os
def retorna_arquivo(request_path,dir):
        # Monta o caminho completo do arquivo a ser acessado
        file_path = os.path.join(dir, request_path[1:])

        if os.path.isfile(file_path):
            # Se o caminho corresponder a um arquivo, lê o conteúdo do arquivo e obtém o tamanho
            with open(file_path, 'rb') as file:
                file_content = file.read()
            file_size = os.path.getsize(file_path)

            # Cria uma resposta para download de arquivo com as informações necessárias
            response = b'HTTP/1.1 200 OK\r\n'
            response += b'Content-Disposition: attachment; filename="' + os.path.basename(file_path).encode('utf-8') + b'"\r\n'
            response += b'Content-type: application/octet-stream\r\n'
            response += b'Content-Length: ' + str(file_size).encode('utf-8') + b'\r\n'
            response += b'\r\n'
            response += file_content
        elif os.path.isdir(file_path):
            # Se o caminho corresponder a um diretório, lista os arquivos e cria uma resposta HTML com os links
            entries = os.listdir(file_path)
            file_list = ''.join([f'<li><a href="{os.path.join(request_path, entry)}">{entry}</a></li>' for entry in entries])

            response = b'HTTP/1.1 200 OK\r\n'
            response += b'Content-type: text/html\r\n'
            response += b'\r\n'
            response += bytes(f'<ul>{file_list}</ul>', encoding='utf-8')
        else:
            # Se o caminho não corresponder a um arquivo nem a um diretório, retorna uma resposta de arquivo não encontrado
            response = b'HTTP/1.1 404 Not Found\r\n'
            response += b'Content-type: text/plain\r\n'
            response += b'\r\n'
            response += b'File not found'

        # Retorna a resposta como uma sequência de bytes
        return response
