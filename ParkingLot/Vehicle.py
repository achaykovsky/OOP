from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, plate_number, vehicle_type):
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type

    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod
    def get_vehicle_plate_number(self):
        pass
