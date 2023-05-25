from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self) -> None:
        self.surface = None
        self.speed = None
    
    def move(self) -> None:
        print(f"Vehicle is driving on {self.surface} with speed: {self.speed}")

    def set_surface(self, surface:str):
        self.surface = surface
    
    def set_speed(self, speed: int):
        self.speed = speed
    
class VehicleBuilder(ABC):
    @abstractmethod
    def create(self, speed: int):
        pass
    
class BoatBuilder(VehicleBuilder):
    def create(speed: int) -> Vehicle:
        vehicle = Vehicle()
        vehicle.set_surface("water")
        vehicle.set_speed(speed)
        return vehicle

class CarBuilder(VehicleBuilder):
    def create(speed: int) -> Vehicle:
        vehicle = Vehicle()
        vehicle.set_surface("road")
        vehicle.set_speed(speed)
        return vehicle
    
if __name__ == "__main__":
    car = CarBuilder.create(80)
    boat = BoatBuilder.create(40)
    car.move()
    boat.move()
