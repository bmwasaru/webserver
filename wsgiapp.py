def app(environ, start_response):
    """Barebone WSGI application
    This is the starting point for your own web framework
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello world from a simple WSGI application!\n']