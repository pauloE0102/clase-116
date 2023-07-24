from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    name = 'Danna'
    return render_template('home.html', student_name = name)

@app.route('/about')
def about():
    return 'About Page'


if __name__ =='__main__':
    app.run()