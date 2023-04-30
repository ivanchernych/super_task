import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/distribution')
def training():
    list = ['иван', 'олег', 'игорь', 'петр']
    return flask.render_template('base.html', list=list)


if __name__ == '__main__':
    app.run(port=8080,  host='127.0.0.1')
