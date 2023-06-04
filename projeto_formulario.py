from bottle import jinja2_view, route, run, request, response

@route('/<area>')
@jinja2_view('paginas/teste.html')
def testes(area):
    return dict(nome=area)

@route('/user', method='GET')
@jinja2_view('paginas/user.html')
def user():
    links = ['honeypot', 'admin', 'user']
    return dict(links=links)

run(port=8080, debug=True)