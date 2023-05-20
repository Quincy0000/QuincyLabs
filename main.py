import time

class TrafficLight:
    def __init__(self):
        self.state = "red"
        self.timer = 0

    def start_timer(self, duration):
        self.timer = duration
        while self.timer > 0:
            print("Traffic light:", self.state)
            time.sleep(1)
            self.timer -= 1

    def set_state(self, state):
        self.state = state

class PedestrianLight:
    def __init__(self):
        self.state = "don't walk"
        self.timer = 0

    def start_timer(self, duration):
        self.timer = duration
        while self.timer > 0:
            print("Pedestrian light:", self.state)
            time.sleep(1)
            self.timer -= 1

    def set_state(self, state):
        self.state = state

class TrafficLightController:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.pedestrian_light = PedestrianLight()

    def run(self):
        while True:

            self.traffic_light.set_state("red")
            self.traffic_light.start_timer(3)

            self.pedestrian_light.set_state("walk")
            self.pedestrian_light.start_timer(2)

            self.pedestrian_light.set_state("don't walk")
            self.pedestrian_light.start_timer(2)

            self.traffic_light.set_state("green")
            self.traffic_light.start_timer(5)

            self.traffic_light.set_state("yellow")
            self.traffic_light.start_timer(2)

# Create an instance of TrafficLightController
controller = TrafficLightController()

# Run the traffic light sequence
controller.run()