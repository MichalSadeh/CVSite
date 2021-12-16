from flask import Flask, redirect, url_for, render_template

app = Flask(_name_)

@app.route('/')
def homepage():
    return render_template('CV1.html')

@app.route('/assignment8')
def ass8():
    return render_template('assignment8.html', firstName='Michal', lastName='Sadeh',
                           hobbies=('dancing', 'singing', 'baking'))


if _name_ == '_main_':
    app.run(debug=True)