def header(request):
    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-type: text/plain\r\n'
    response += b'\r\n'
    response += bytes(request, encoding='utf-8')
    return response