from machine import Pin
import time
from Model import Model, MOTION_DETECTED, MOTION_ENDED
from Sensors import DigitalSensor

class VehicleDetectionHandler:
    """
    Handler class for the vehicle detection state model
    Implements the stateEntered, stateLeft, and stateDo methods
    """

    def stateEntered(self, state):
        print(f"Entered state {state}")
        if state == 1:
            print("Waiting at pedestrian crossing")
        elif state == 2:
            print("Vehicle stopped for crossing")
        elif state == 3:
            print("Vehicle crossed the pedestrian crossing")
        elif state == 4:
            print("Vehicle moving away from crossing")

    def stateLeft(self, state):
        print(f"Left state {state}")

    def stateDo(self, state):
        pass

# Initialize the PIR motion sensor on pin 10
pir_sensor = DigitalSensor(26)

# Create the vehicle detection model with 5 states
model = Model(5, VehicleDetectionHandler(), debug=True)

# Add transitions for the model
model.addTransition(0, MOTION_DETECTED, 1)
model.addTransition(1, MOTION_ENDED, 2)
model.addTransition(2, MOTION_DETECTED, 3)
model.addTransition(3, MOTION_ENDED, 4)
model.addTransition(4, MOTION_DETECTED, 0)

# Start the model
model.start()

# Continuously monitor the PIR motion sensor and process events
while True:
    if pir_sensor.tripped():
        model.processEvent(MOTION_DETECTED)
    else:
        model.processEvent(MOTION_ENDED)
    
    time.sleep(0.1)