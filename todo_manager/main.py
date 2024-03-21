from flask import Flask, request

app = Flask(__name__)

header = open('templates/page_header.html', 'r').read()
footer = open('templates/page_footer.html', 'r').read()

form = open('templates/todo_form.html', 'r').read()

doings = []


@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        doings.append(request.form['doing'])

    todos = '<ul>'

    for doing in doings:
        todos += '<li>' + doing + '</li>'

    todos += '</ul>' + '<br>'

    return header + todos + form + footer
