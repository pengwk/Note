from wsgiref.simple_server import make_server

def application(environ, start_response):
  response_body = 'hahaha'
  status = '200 OK'
  response_headers = [
    ('Content-Type', 'text/plain'),
    ('Content-Length', str(len(response_body)))
  ]
  start_response(status, response_headers)
  return [response_body]

httpd = make_server(
  'localhost',
  8888,
  application,
)
httpd.handle_request()
