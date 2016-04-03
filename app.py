# Simple implementation of picamera + flask
from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, request
from utils import generate_filename

import time
import picamera

app = Flask(__name__)
# Change here (for flash)
app.secret_key = 'my_secret_lol'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/snap', methods=['GET', 'POST'])
def snap():
    '''
    take image using pi camera
    Save to /static/images/image-**timestamp**.jpg
    '''
    if request.method == 'POST':
        image = Image()
        filename = image.snap()
        flash('Image captured in ' + filename)
        return redirect(url_for('snap', filename=filename))
    else:
        return render_template('snap.html', filename=request.args.get('filename'))

@app.route('/shoot', methods=['GET', 'POST'])
def shoot():
    '''
    shoot a video
    save to /static/videos/video-**timestamp**.h264
    '''
    if request.method == 'POST':
        video = Video()
        filename = video.shoot()
        flash('Video recorded in ' + filename)
        return redirect(url_for('shoot', filename=filename))
    else:
        return render_template('shoot.html', filename=request.args.get('filename'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
