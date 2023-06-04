from bottle import get, post, run, request, template

@get('/')
def index_get():
    return '''
    <form action="/" method="POST">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
    </form>'''

@post('/')
def index_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return '''
    <h1> Suas informações de login são: </h1>
    <p> Username: {} </p>
    <p> Password: {} </p>'''.format(username, password)

run(host='localhost', port=8080)