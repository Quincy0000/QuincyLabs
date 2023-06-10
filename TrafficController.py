from machine import Pin
from time import sleep
from Displays import LCDDisplay
from CompositeLights import TrafficLight
from Buzzer import ActiveBuzzer

class Light:
    def _init_(self, pin, name):
        self.pin = pin
        self.name = name
        self.led = Pin(self.pin, Pin.OUT)
        self.off()  # Turn off the LED initially
    
    def on(self):
        self.led.on()
    
    def off(self):
        self.led.off()
    
    def _str_(self):
        return f"{self.name} (Pin {self.pin})"

# Create instances of the lights connected to GPIO pins
tl1_red_led = Light(0, "TL1 Red LED")
tl1_yellow_led = Light(1, "TL1 Yellow LED")
tl1_green_led = Light(2, "TL1 Green LED")

tl2_red_led = Light(3, "TL2 Red LED")
tl2_yellow_led = Light(4, "TL2 Yellow LED")
tl2_green_led = Light(5, "TL2 Green LED")

# Create an instance of the traffic light for TL1 with the LED instances
traffic_light1 = TrafficLight(tl1_red_led, tl1_yellow_led, tl1_green_led)

# Create an instance of the traffic light for TL2 with the LED instances
traffic_light2 = TrafficLight(tl2_red_led, tl2_yellow_led, tl2_green_led)

# Create an instance of the LCD display for TL1
display1 = LCDDisplay(sda=20, scl=21, i2cid=0)

# Create an instance of the LCD display for TL2
display2 = LCDDisplay(sda=22, scl=27, i2cid=1)

# Create an instance of the active buzzer
buzzer = ActiveBuzzer(6)  # Assuming pin 6 is connected to the buzzer

# Function to display the pedestrian crossing state on the LCD displays
def display_pedestrian_state(state1, state2):
    display1.showText(state1)
    display2.showText(state2)

# Function to control the traffic light sequence
def control_traffic_lights():
    # Loop indefinitely
    while True:
        # TL1: Red, TL2: Green
        tl1_red_led.on()
        tl1_yellow_led.off()
        tl1_green_led.off()
        tl2_red_led.off()
        tl2_yellow_led.off()
        tl2_green_led.on()
        display_pedestrian_state("Don't Walk", "Walk")
        sleep(10)
        
        # TL1: Red, TL2: Yellow
        tl1_red_led.on()
        tl1_yellow_led.off()
        tl1_green_led.off()
        tl2_red_led.off()
        tl2_yellow_led.on()
        tl2_green_led.off()
        display_pedestrian_state("Don't Walk", "Don't Walk")
        sleep(8)
        
        # TL1: Green, TL2: Red
        tl1_red_led.off()
        tl1_yellow_led.off()
        tl1_green_led.on()
        tl2_red_led.on()
        tl2_yellow_led.off()
        tl2_green_led.off()
        display_pedestrian_state("Walk", "Don't Walk")
        sleep(10)
        
        # TL1: Yellow, TL2: Red
        tl1_red_led.off()
        tl1_yellow_led.on()
        tl1_green_led.off()
        tl2_red_led.on()
        tl2_yellow_led.off()
        tl2_green_led.off()
        display_pedestrian_state("Don't Walk", "Don't Walk")
        sleep(10)
        
        # Buzz the buzzer for pedestrian crossing
        buzzer.beep(tone=1000, duration=2000)

# Start controlling the traffic lights
control_traffic_lights()