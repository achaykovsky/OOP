from ParkingLot.ParkingSpot import ParkingSpot
from ParkingLot.SpotType import SpotType
from ParkingLot.Vehicle import Vehicle
from ParkingLot.VehicleType import VehicleType


class Level:
    def __init__(self, total_num_of_spots):
        self.total_num_of_spots = total_num_of_spots
        self.occupied_status = False
        self.current_occupied_places = 0
        self.parking_spots = []

        # initializing with empty spots the level with equal numbers of parking spots
        for i in range(self.total_num_of_spots):
            if i % 3 == 0:  # motorcycle
                self.parking_spots.append(ParkingSpot(i, SpotType.small))
            elif i % 3 == 1:  # car
                self.parking_spots.append(ParkingSpot(i, SpotType.medium))
            else:  # bus
                self.parking_spots.append(ParkingSpot(i, SpotType.large))

    def get_total_num_of_spots(self):
        return self.total_num_of_spots

    def get_current_occupied_places(self):
        return self.current_occupied_places

    def get_parking_spots(self):
        return self.parking_spots

    def set_occupied_status(self):
        if self.total_num_of_spots == self.current_occupied_places:
            self.occupied_status = True
        else:
            self.occupied_status = False

    def get_occupied_status(self):
        return self.occupied_status

    def find_available_place_for_vehicle(self, vehicle):
        if self.occupied_status:
            print(f"No available places on this level")
            return -1
        for i in range(len(self.parking_spots)):
            vehicle_spot_size = self.find_available_spot_per_vehicle_type(vehicle)
            if i % 3 == vehicle_spot_size and not self.parking_spots[i].get_occupied_status():
                return i
        return -1

    def find_available_spot_per_vehicle_type(self, vehicle: Vehicle):
        parking_spot = -1
        vehicle_type = vehicle.get_vehicle_type()
        if vehicle_type == VehicleType.CAR:
            parking_spot = SpotType.medium.value  # 1
        elif vehicle_type == VehicleType.MOTORCYCLE:
            parking_spot = SpotType.small.value  # 0
        elif vehicle_type == VehicleType.BUS:
            parking_spot = SpotType.large.value  # 2
        else:
            TypeError("This vehicle is not permitted")
        return parking_spot

    def park_vehicle(self, spot, vehicle):
        parking_spot_type = self.find_available_spot_per_vehicle_type(vehicle)
        if spot >= 0:
            self.parking_spots[spot] = ParkingSpot(spot, parking_spot_type)
            self.parking_spots[spot].set_vehicle_to_parking_spot(vehicle.get_vehicle_plate_number())
        else:
            print(f"Could not park vehicle. Please look for a parking spot on another level")
