from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config['SERVER_NAME'] = 'localhost:8000'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/mlmodels')
def mlmodels():
    return(render_template('mlmodels.html'))

@app.route('/dlmodels')
def dlmodels():
    return render_template('dlmodels.html')
    

@app.route('/eda')
def eda():
    return render_template('eda.html')

if __name__ == '__main__':
    app.run(debug=True)