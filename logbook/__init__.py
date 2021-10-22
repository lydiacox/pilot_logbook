from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/pilots/')
def get_pilots():
    return 'This will be a list of all the pilots.'

@app.route('/pilots/<int:pilot_id>/')
def get_specific_pilots(pilot_id):
    return f'This will be a page displaying information about pilot {pilot_id}.'

@app.route('/calc/<int:f_num>/<string:operator>/<int:s_num>')
def calculate(f_num, operator, s_num):
    if operator in ['+', '-', '*', '/']:
        return f"{eval(f'{f_num}{operator}{s_num}')}"
    return "Please enter a valid calculation"

if __name__ == '__main__':
    app.run(debug=True)