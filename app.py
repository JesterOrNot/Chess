from flask import Flask, render_template
app = Flask(__name__, static_folder='.', template_folder='./site')
@app.route('/')
def java():
    return app.send_static_file('./site/myapplet.html')
@app.route('/hello/')
def hello():
    return app.send_static_file('./site/hello.html')
@app.route('/magic/')
def magic():
    return app.send_static_file('./site/my-file.html')
@app.route('/readme/')
def readme():
    return app.send_static_file('./site/readme.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')
