def header(request):
    # Cria uma resposta de cabeçalho simples com o conteúdo da solicitação
    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-type: text/plain\r\n'
    response += b'\r\n'
    response += bytes(request, encoding='utf-8')
    return response