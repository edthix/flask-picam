from flask import Flask, render_template, redirect, url_for
from time import gmtime, strftime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/snap', methods=['POST'])
def snap():
    # take image using pi camera
    # Save to /static/images/image-**timestamp**.jpg
    filename = "image-" + strftime("%Y%m%d%H%M%S", gmtime()) + ".jpg"
    #return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)