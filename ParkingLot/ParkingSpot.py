class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.occupied_status = False
        self.vehicle_id = -1
        self.spot_type = spot_type

    def set_occupied_status(self, occupied_status):
        self.occupied_status = occupied_status

    def get_occupied_status(self):
        return self.occupied_status

    def get_vehicle_id(self):
        return self.vehicle_id

    def remove_vehicle_from_spot(self):
        self.vehicle_id = -1
        self.set_occupied_status(False)

    def set_vehicle_to_parking_spot(self, vehicle_id):
        if not self.occupied_status:
            self.vehicle_id = vehicle_id
            self.set_occupied_status(True)
