from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, request
import time
import picamera

app = Flask(__name__)
app.secret_key = 'my_secret_lol' # for flash

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
        filename = generate_filename('jpg')
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture(filename)
            camera.stop_preview()    
            
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
        filename = generate_filename('h264', 'videos')
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview()
            camera.start_recording(filename)
            camera.wait_recording(10)
            camera.stop_recording()
            camera.stop_preview()
            
        flash('Video recorded in ' + filename)
        return redirect(url_for('shoot', filename=filename))
    else:
        return render_template('shoot.html', filename=request.args.get('filename'))


def generate_filename(filetype='', folder='images'):
    '''
    Generate a timestamped filename
    filetype = jpg, gif, etc.
    '''
    filename = 'static/' + folder + '/image-' + time.strftime("%Y%m%d%H%M%S", time.gmtime()) + '.' + filetype
    return filename

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
