from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def hello():
   stuff="<strong> this  is stuff</strong> "
   li=["pizza","burger","poop corn","fries"]
   return render_template("index.html",stuff=stuff,li=li)

@app.route('/<name>')
def hello_name(name):
   return render_template("user.html",user=name)

if __name__ == '__main__':
   app.run(debug = True)    