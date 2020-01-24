from __future__ import division
import time
import Adafruit_PCA9685

from tkinter import *

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale_pan = Scale(frame, label="pan", from_=0, to=180, tickinterval=90, orient=HORIZONTAL, command=self.update_pan)
        scale_pan.set(90)
        scale_pan.grid(row=0, column=0)
        scale_tilt = Scale(frame, label="tilt", from_=0, to=180, tickinterval=90, orient=VERTICAL, command=self.update_tilt)
        scale_tilt.set(90)
        scale_tilt.grid(row=0, column=1)

    def update_pan(self, angle):
        duty = int( float(angle) * 2.17 + 102 )
        pwm.set_pwm(0, 0, duty)
        time.sleep(0.1)

    def update_tilt(self, angle):
        duty = int( float(angle) * 2.17 + 102 )
        pwm.set_pwm(1, 0, duty)
        time.sleep(0.1)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("220x120+0+0")
root.mainloop()
