from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/tweetflow')
def tweetflow():
    return render_template('tweetflow.html')


if __name__ == '__main__':
    app.run()
