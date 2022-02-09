from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def frst():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return """<p>Человечество вырастает из детства.</p>
<p>Человечеству мала одна планета.</p>
<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
<p>И начнем с Марса!</p>
<p>Присоединяйся!</p>"""


@app.route('/image_mars')
def img():
    return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Привет, Марс!</title>
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            </head>
            <body>
                <h1>Жди нас, Марс!</h1>
                <figure>
                    <img 
                        src='/static/img/MARS.png' 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <figcaption>
                      "Вот она какая, красная планета"
                    </figcaption>
                </figure>
                
            </body>
            </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>

    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <figure>
        <img 
            src='/static/img/MARS.png' 
            alt="здесь должна была быть картинка, но не нашлась">
        <figcaption>
          "Вот она какая, красная планета"
        </figcaption>
    </figure>
    <div class="alert alert-dark" role="alert">
        Человечество вырастает из детства.
    </div>
    <div class="alert alert-success" role="alert">
        Человечеству мала одна планета.
    </div>
    <div class="alert alert-secondary" role="alert">
        Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-warning" role="alert">
        И начнем с Марса!
    </div>
    <div class="alert alert-danger" role="alert">
        Присоединяйся!
    </div>
    
</body>
</html>"""


@app.route('/astronaut_selection')
def astronaut_slection():
    if request.method == 'GET':
        return f"""<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Привет, Марс!</title>
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    </head>
                    <body>
                        <h1>Анкета претендента</h1>
                        <h2>на участе в миссии</h2>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" placeholder="Введите фамилию">
                                <input type="text" class="form-control" placeholder="Введите имя">
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                
                                <div class="form-group">
                                    <label for="classSelect">Какое у вас образование?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>Начальное</option>
                                      <option>Среднее</option>
                                      <option>Высшее</option>
                                    </select>
                                 </div>
                    
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input">
                                    <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input">
                                    <label class="form-check-label" for="acceptRules">пилот</label>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input">
                                    <label class="form-check-label" for="acceptRules">врач</label>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input">
                                    <label class="form-check-label" for="acceptRules">метеоролог</label>
                                </div>
                    
                                 <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                    
                                <div class="form-group">
                                    <label for="about">Почему вы хотите принять участие в миссии?</label>
                                    <textarea class="form-control" id="motivation" rows="3"></textarea>
                                </div>
                    
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                    
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input">
                                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                </div>
                                
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                        
                    </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')