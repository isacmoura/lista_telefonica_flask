from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.jinja2')

@app.route('/demo')
def demo():
    return render_template('demo.jinja2')
    
app.run(debug=True)