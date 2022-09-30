from flask import render_template, request

def routes(route="index"):

    return render_template(
            f"{route}.html")

def add():

    n1 = int(request.form.get('n1'))
    n2 = int(request.form.get('n2'))
    
    return str(n1 + n2)

def hello():

    user = request.form.get('user')
    return f"Hello, {user}!"