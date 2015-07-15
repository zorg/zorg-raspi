from zorg.adaptor import Adaptor
from RPi import GPIO


class RasPi(Adaptor):

    def __init__(self, options):
        super(RasPi, self).__init__(options)
        
        GPIO.setmode(GPIO.BOARD)
        
    def digital_write(self, pin_number, value):
        GPIO.setup(pin_number, GPIO.OUT)
        
        GPIO.output(pin_number, value)
