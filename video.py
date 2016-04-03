import picamera
from utils import generate_filename

class Video:
    """ Video stuffs """

    def shoot(self):
        """
        Shoots a video and saves it to /static/videos/video-**timestamp**.h264
        """
        filename = generate_filename('h264', 'videos')
        with picamera.Picamera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview()
            camera.start_recording(filename)
            camera.wait_recording(10)
            camera.stop_recording()
            camera.stop_preview()

        return filename
