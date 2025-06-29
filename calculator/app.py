from flask import Flask, url_for, render_template, redirect, request
from logic import calculator

app = Flask(__name__)
app.config['SECRET_KEY'] = '7670d63b93296b5ac9cc55ca096dd9db'

@app.route("/",methods=['GET','POST'])
def calculate_route():
    result = None
    
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        operation = request.form['operator']
        num2 = float(request.form['num2']) if request.form['num2'] else None
        result = calculator(num1,num2,operation)

    return render_template('index.html',result = result)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=10000)
    