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


@app.route('/astronaut_slection')
def astronaut_slection():
    if request.method == 'GET':
        return


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')