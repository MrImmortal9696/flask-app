from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
   return "<h1>App runnnning <h1>"

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)    