from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages
import time
import picamera

app = Flask(__name__)
app.secret_key = 'my_secret_lol' # for flash

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/snap', methods=['POST'])
def snap():
    # take image using pi camera
    # Save to /static/images/image-**timestamp**.jpg
    filename = "static/images/image-" + time.strftime("%Y%m%d%H%M%S", time.gmtime()) + ".jpg"
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(filename)
        camera.stop_preview()

    flash('Image captured in ' + filename)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
