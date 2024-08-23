from ParkingLot.Vehicle import Vehicle
from ParkingLot.VehicleType import VehicleType


class Car(Vehicle):
    def __init__(self, plate_number: str):
        super().__init__(plate_number, VehicleType.CAR)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_vehicle_plate_number(self):
        return self.plate_number