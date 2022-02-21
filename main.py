from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('template.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('engineer.html', title='Name', prof=prof)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    return render_template('list_prof.html', title='Name', type_list=type_list)


autor_answer_data = {'title': 'title',
    'surname': 'surname',
    'name': 'name',
    'education': 'education',
    'profession': 'profession',
    'sex': 'sex',
    'motivation': 'motivation',
    'ready': 'ready',
}


# ИЗ КАКОГО ОБРАБОТЧИКА БЕРУТЬСЯ ДАННЫЕ????
@ app.route('/answer')
@ app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', title=autor_answer_data['title'], autor_answer_data=autor_answer_data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')