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
    return """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Привет, Марс!</title>
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')