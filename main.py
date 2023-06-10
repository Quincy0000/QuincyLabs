import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")


from PedestrianCrossing import PedestrianCrossing
from TrafficLightController import Light
from vehicle import VehicleDetectionHandler

if _name_ == "_main_":
    crossing = PedestrianCrossing()
    crossing.run()

    traffic_light = TrafficLightController()
    traffic_light.control_traffic_lights()

    vehicle_handler = VehicleDetectionHandler()