from flask import Flask, render_template

APP = Flask(__name__, static_folder='.', template_folder='./site')
@APP.route('/')
def java():
    return APP.send_static_file('./site/myapplet.html')


@APP.route('/hello/')
def hello():
    return APP.send_static_file('./site/hello.html')


@APP.route('/magic/')
def magic():
    return APP.send_static_file('./site/my-file.html')


@APP.route('/readme/')
def readme():
    return APP.send_static_file('./site/readme.html')


@APP.route('/chess/')
def board():
    return APP.send_static_file('./site/new.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port='3000')
