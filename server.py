from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lists')
def home():

    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template('index.html', users=users)

@app.errorhandler(404)
def my_error(err_no):
    return f"{err_no}"

if __name__=="__main__":
    app.run(debug=True)