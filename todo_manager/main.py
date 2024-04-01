from flask import Flask, request

app = Flask(__name__)

header = open('templates/page_header.html', 'r').read()
footer = open('templates/page_footer.html', 'r').read()

form = open('templates/todo_form.html', 'r').read()


def get_todo_edit_form(idx: int) -> str:
    return f'''
    <form action="/" method="post">
        <input type="hidden" name="delete_doing" value="{idx}">
        <input type="submit" value="X">
    </form>
    '''


def get_todos(doings: list) -> str:
    todos = '<ul>'

    for idx, doing in enumerate(doings):
        todos += ('<li>' + doing + get_todo_edit_form(idx) + '</li>')

    todos += '</ul>' + '<br>'

    return todos


@app.route('/', methods=['GET', 'POST'])
def main() -> str:
    todos_file = open('todos.txt', 'r')
    doings = todos_file.readlines()
    todos_file.close()

    if request.method == 'POST':
        if 'add_doing' in request.form and request.form['add_doing'] != '':
            doings.append(request.form['add_doing'])
        if 'delete_doing' in request.form:
            del doings[int(request.form['delete_doing'])]

    todos = get_todos(doings)

    todos_file = open('todos.txt', 'w')
    todos_file.writelines(doings)
    todos_file.close()

    return header + todos + form + footer
