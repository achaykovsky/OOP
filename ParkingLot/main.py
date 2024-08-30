from ParkingLot.Motorcycle import Motorcycle
from ParkingLot.ParkingLot import ParkingLot

###### Design a parking Lot #####
# We have three types of vehicles: Car, Motorcycle, Bus
# The parking lot can have more than one level
# Each level has parking spots
# Each type of vehicle has its own size and should have a designated size parking spot to park there
# We have equal number of spots for each kind of vehicle


if __name__ == '__main__':
    tel_aviv_parking_lot = ParkingLot(num_of_levels=3, total_num_of_spots=9)

    motorcycle1 = Motorcycle("JKHT5")
    motorcycle2 = Motorcycle("JKHT52")
    motorcycle3 = Motorcycle("JKHT53")
    motorcycle4 = Motorcycle("JKHT54")
    motorcycle5 = Motorcycle("JKHT55")

    # bus = Bus("JKHTML5")
    # motorcycle = Motorcycle("HTDOP5")
    tel_aviv_parking_lot.add_vehicle_to_parking_lot(motorcycle1)
    tel_aviv_parking_lot.add_vehicle_to_parking_lot(motorcycle2)
    tel_aviv_parking_lot.add_vehicle_to_parking_lot(motorcycle3)
    tel_aviv_parking_lot.add_vehicle_to_parking_lot(motorcycle4)
    tel_aviv_parking_lot.add_vehicle_to_parking_lot(motorcycle5)

    print("success")
