from bottle import request, route, run, response

@route('/')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    response.set_cookie("visited", "yes")
    return "Hello there! Nice to meet you"

run(host='localhost', port=8080)