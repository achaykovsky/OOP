from Level import Level


class ParkingLot:
    def __init__(self, num_of_levels, total_num_of_spots):
        self.num_of_levels = num_of_levels
        self.levels = []

        # initializing levels in the parking lot
        for i in range(num_of_levels):
            self.levels.append(Level(total_num_of_spots))

    def get_num_levels(self):
        return self.num_of_levels

    def add_vehicle_to_parking_lot(self, vehicle):
        for i, level in enumerate(self.levels):
            spot = level.find_available_place_for_vehicle(vehicle)
            if spot >= 0:
                level.park_vehicle(spot, vehicle)
                print(
                    f"The vehicle {vehicle.get_vehicle_plate_number()} was parked at spot number:{spot} on floor: {i}")
                break
            else:
                if i != self.num_of_levels - 1:
                    print("Trying to park at the next level")
                    continue
                else:
                    print("Unable to park the vehicle")

    def remove_vehicle_from_parking_lot(self, vehicle):
        vehicle_plate_number = vehicle.get_vehicle_plate_number()
        for i, level in enumerate(self.levels):
            for spot in level.get_parking_spots():
                if spot.get_vehicle_id() == vehicle_plate_number:
                    spot.remove_vehicle_from_spot()
                    print(f"The vehicle {vehicle_plate_number} was removed from {i}")

        print(f"The plate number {vehicle_plate_number} was not found")
