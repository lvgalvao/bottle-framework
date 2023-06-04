"""
um exemplo de aplicação web simples usando Bottle com rotas dinâmicas e estáticas.
"""

from bottle import route, run, template

@route('/')
def index():
    """Rota estática para index do site."""
    return '<h1>Olá, mundo!</h1>'

@route('/<person>')
def index(person):
    """Exemplo de rota dinâmica."""
    if person == 'Marivaldo':
        return 'Você não é bem vindo Marivaldo'
    return template('<h1>Olá, {{person}}!</h1>', person=person)

run(host='localhost', port=8080)