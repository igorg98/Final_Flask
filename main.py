from flask import Flask, render_template, request
from FirstEx import TrbuttunClicked
from ThirdEx import Cube

app = Flask(__name__)

@app.route('/first', methods=['GET', 'POST'])
def first():
    if request.method == 'POST':
        input = request.form['input']
        return render_template('first.html', out=TrbuttunClicked(input))
    return render_template('first.html', out='')



cube = Cube(10)
@app.route('/third', methods=['GET', 'POST'])
def third():
    if request.method == 'POST':
        if request.form['btndo'] == 'btndo':
            cube.Pimp_by_X(request.form['x'])
            cube.Pimp_by_Y(request.form['y'])
            cube.Pimp_by_Z(request.form['z'])
        return render_template('third.html', output=cube)
    return render_template('third.html')

@app.route('/')
def index():
    return render_template('main.html')
