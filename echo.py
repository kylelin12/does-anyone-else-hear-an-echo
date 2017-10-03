from flask import Flask, render_template, request

echo_app = Flask(__name__)

@echo_app.route('/')
def root():
    return render_template('echo_form.html')

# The /echo page uses the POST method and has username and method as arguments
@echo_app.route('/echo', methods=["POST", "GET"])
def echo():
    if request.method == 'POST':
        username = request.form['username']
        method = 'POST'
    else:
        username = request.args['username']
        method = 'GET'
    return render_template('echo_echo.html', username = username, method = method)

if __name__ == '__main__':
    echo_app.debug = True
    echo_app.run()