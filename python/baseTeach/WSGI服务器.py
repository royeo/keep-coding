# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
# HTTP请求的所有输入信息都可以通过environ获得
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()