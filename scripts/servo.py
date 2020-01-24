import time
        
class PCA9685:
    ''' 
    PWM motor controler using PCA9685 boards. 
    This is used for most RC Cars
    '''
    def __init__(self, channel, address=0x40, frequency=60, busnum=None, init_delay=0.1):

        self.default_freq = 60
        self.pwm_scale = frequency / self.default_freq

        import Adafruit_PCA9685
        # Initialise the PCA9685 using the default address (0x40).
        if busnum is not None:
            from Adafruit_GPIO import I2C
            # replace the get_bus function with our own
            def get_bus():
                return busnum
            I2C.get_default_bus = get_bus
        self.pwm = Adafruit_PCA9685.PCA9685(address=address)
        self.pwm.set_pwm_freq(frequency)
        self.channel = channel
        time.sleep(init_delay) # "Tamiya TBLE-02" makes a little leap otherwise

    def set_pulse(self, pulse):
        try:
            self.pwm.set_pwm(self.channel, 0, int(pulse * self.pwm_scale))
        except:
            self.pwm.set_pwm(self.channel, 0, int(pulse * self.pwm_scale))

    def run(self, pulse):
        self.set_pulse(pulse)

#9865, over rides only if needed, ie. TX2..
PCA9685_I2C_ADDR = 0x40
PCA9685_I2C_BUSNUM = None

#STEERING
STEERING_CHANNEL = 1
STEERING_LEFT_PWM = 460
STEERING_RIGHT_PWM = 290

class PWMSteering:
    """
    Wrapper over a PWM motor controller to convert angles to PWM pulses.
    """
    LEFT_ANGLE = -1
    RIGHT_ANGLE = 1

    def __init__(self,
                 controller=None,
                 left_pulse=290,
                 right_pulse=490):

        self.controller = controller
        self.left_pulse = left_pulse
        self.right_pulse = right_pulse
    #    self.pulse = dk.utils.map_range(0, self.LEFT_ANGLE, self.RIGHT_ANGLE,
    #                                    self.left_pulse, self.right_pulse)
        self.running = True
        print('PWM Steering created')

    def update(self):
        while self.running:
            self.controller.set_pulse(self.pulse)

    def run_threaded(self, angle):
        # map absolute angle to angle that vehicle can implement.
    #    self.pulse = dk.utils.map_range(angle,
    #                                    self.LEFT_ANGLE, self.RIGHT_ANGLE,
    #                                    self.left_pulse, self.right_pulse)
        pass

    def run(self, angle):
        self.run_threaded(angle)
        self.controller.set_pulse(self.pulse)

    def shutdown(self):
        # set steering straight
        self.pulse = 0
        time.sleep(0.3)
        self.running = False

if __name__ == "__main__":
    steering_controller = PCA9685(STEERING_CHANNEL, PCA9685_I2C_ADDR, busnum=PCA9685_I2C_BUSNUM)

    while True:
        steering_controller.set_pulse(60)

        steering_controller.set_pulse(200)
        time.sleep(1)
        steering_controller.set_pulse(400)
        time.sleep(1)

#    steering = PWMSteering(controller=steering_controller,
#                                    left_pulse=STEERING_LEFT_PWM, 
#                                    right_pulse=STEERING_RIGHT_PWM)    
     