from bottle import route, run, template, get, post, request
from cgi import escape


def html_table(t):  
    s = """<table border="1">"""
    for r in range(1, t + 1):
        s += """<tr>"""
        for c in range(1, t + 1):
            s += """<td>""" + escape(str(r * c)) + """</td>"""
        s += """</tr>"""
    s += """</table>"""
    return s


@get('/start')  # or @route('/start')
def start():
    return '''
        <form action="/print_square" method="post">
            square: <input name="square_size" type="text" value="10"/>
            <input value="Login" type="submit" />
        </form>
    '''


@post('/print_square')  # or @route('/print_square', method='POST')
def print_square():
    square_size = int(request.forms.get('square_size'))
    if square_size == 0:
        return "Error"
    else:
        return html_table(square_size)


# run(host='localhost', port=8080)




