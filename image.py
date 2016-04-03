import picamera
from utils import generate_filename

class Image:
    """ Image stuffs """

    def snap(self):
        """
        Snap an image and saves it to /static/images/image-**timestamp**.jpg
        """
        filename = generate_filename("jpg")
        with picamera.Picamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture(filename)
            camera.stop_preview()

        return filename
