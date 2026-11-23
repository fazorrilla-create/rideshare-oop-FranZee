class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0  
        self.__total_trips = 0

    def add_rating(self, new_rating):
        if new_rating < 1 or new_rating > 5:
            raise ValueError("Invalid rating!")

        if self.__total_trips == 0:
            self.__rating = new_rating
        else:
            self.__rating = (self.__rating * self.__total_trips + new_rating) / (self.__total_trips + 1)

        self.__total_trips += 1

    def get_rating_info(self):
        return f"Dreiver: {self.__rating:.2f}/5.0 | Total Trips: {self.__total_trips}"
