from machine import Pin
from time import sleep
from Displays import LCDDisplay
from Button import Button

class PedestrianCrossing:
    def _init_(self):
        self.button1_pin = 28  # GPIO pin connected to button 1
        self.button2_pin = 17  # GPIO pin connected to button 2
        self.pull_type = Pin.PULL_DOWN  # Specify the pull type
        self.display1_sda = 20  # I2C SDA pin connected to display 1
        self.display1_scl = 21  # I2C SCL pin connected to display 1
        self.display2_sda = 22  # I2C SDA pin connected to display 2
        self.display2_scl = 27  # I2C SCL pin connected to display 2
        self.button1 = Button(self.button1_pin, self.pull_type, buttonhandler=self)
        self.button2 = Button(self.button2_pin, self.pull_type, buttonhandler=self)
        self.display1 = LCDDisplay(sda=self.display1_sda, scl=self.display1_scl)
        self.display2 = LCDDisplay(sda=self.display2_sda, scl=self.display2_scl)
        self.button1_pressed = False
        self.button2_pressed = False

    def run(self):
        while True:
            if self.button1_pressed:
                self.display1.showText("Crossing Requested")
            else:
                self.display1.showText("")
            
            if self.button2_pressed:
                self.display2.showText("Crossing Requested")
            else:
                self.display2.showText("")
            
            # Sleep for a short interval
            sleep(0.1)
    
    def buttonPressed(self, name):
        if name == self.button1.getName():
            self.button1_pressed = True
        elif name == self.button2.getName():
            self.button2_pressed = True

    def buttonReleased(self, name):
        if name == self.button1.getName():
            self.button1_pressed = False
        elif name == self.button2.getName():
            self.button2_pressed = False

if _name_ == "_main_":
    crossing = PedestrianCrossing()
    crossing.run()