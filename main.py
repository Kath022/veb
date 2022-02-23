from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

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


@ app.route('/answer')
@ app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', title=autor_answer_data['title'], autor_answer_data=autor_answer_data)


class LoginForm(FlaskForm):
    id_astronaut = StringField('id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])

    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')