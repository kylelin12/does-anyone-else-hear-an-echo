from flask import Flask, render_template, request

echo_app = Flask(__name__)

@echo_app.route('/')
def root():
    return render_template('echo_form.html')

# The /echo page uses the POST method and has username and method as arguments
@echo_app.route('/echo', methods=["POST", "GET"])
def echo():
    return render_template('echo_echo.html', username = request.form['username'], method = request.method)

if __name__ == '__main__':
    echo_app.debug = True
    echo_app.run()