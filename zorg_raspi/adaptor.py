from zorg.adaptor import Adaptor
from RPi import GPIO


class RasPi(Adaptor):

    def __init__(self, options):
        super(RasPi, self).__init__(options)
        
        GPIO.setmode(GPIO.BOARD)
        
        self.pwm = {}
        
    def digital_write(self, pin_number, value):
        GPIO.setup(pin_number, GPIO.OUT)
        
        GPIO.output(pin_number, value)
        
    def pwm_write(self, pin_number, duty_cycle, frequency):
        if pin_number not in self.pwm:
            GPIO.setup(pin_number, GPIO.OUT)
        
            self.pwm[pin_number] = GPIO.PWM(pin_number, frequency)
            self.pwm[pin_number].start(duty_cycle)
            
        pin = self.pwm[pin_number]
        
        pin.ChangeFrequency(frequency)
        pin.ChangeDutyCycle(duty_cycle)
