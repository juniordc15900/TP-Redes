import os
def retorna_arquivo(request_path,dir):
        file_path = os.path.join(dir, request_path[1:])

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_content = file.read()
            file_size = os.path.getsize(file_path)

            response = b'HTTP/1.1 200 OK\r\n'
            response += b'Content-Disposition: attachment; filename="' + os.path.basename(file_path).encode('utf-8') + b'"\r\n'
            response += b'Content-type: application/octet-stream\r\n'
            response += b'Content-Length: ' + str(file_size).encode('utf-8') + b'\r\n'
            response += b'\r\n'
            response += file_content

        elif os.path.isdir(file_path):
            entries = os.listdir(file_path)
            file_list = ''.join([f'<li><a href="{os.path.join(request_path, entry)}">{entry}</a></li>' for entry in entries])

            response = b'HTTP/1.1 200 OK\r\n'
            response += b'Content-type: text/html\r\n'
            response += b'\r\n'
            response += bytes(f'<ul>{file_list}</ul>', encoding='utf-8')
        else:
            response = b'HTTP/1.1 404 Not Found\r\n'
            response += b'Content-type: text/plain\r\n'
            response += b'\r\n'
            response += b'File not found'

        return response
