import os
from flask import Flask, render_template


def get_html(root):
    result = {}

    filenames = os.listdir(os.path.join('templates', root))
    for f in filenames:
        if f.endswith('html'):
            print(os.path.join(root, f))
            result[f[:-5]] = render_template(os.path.join(root, f))

    return result


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/ldy')
def load_ldy():
    return render_template('ldy.html', result=get_html('ldy'))


@app.route('/pjh')
def load_pjh():
    return render_template('pjh.html', result=get_html('pjh'))

@app.route('/sjs')
def load_sjs():
    return render_template('sjs.html', result=get_html('sjs'))


if __name__ == '__main__':
    app.run()
