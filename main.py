from abc import ABC, abstractmethod


class Ride(ABC):
    def __init__(self, distance_km):
        self.distance_km = distance_km
        self.is_completed = False

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def start_ride(self):
        pass

    @abstractmethod
    def complete_ride(self):
        pass


class PassengerAccount:
    def __init__(self, name):
        self.name = name
        self.__wallet_balance = 0.0

    def top_up_wallet(self, amount):
        if amount < 0:
            raise ValueError("Error! Balance is invalid.")
        self.__wallet_balance += amount

    def pay_for_ride(self, fare_amount):
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")
        self.__wallet_balance -= fare_amount
        print("PHP", self.__wallet_balance)


class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0
        self.__total_trips = 0

    def add_rating(self, new_rating):
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Invalid rating!")

        if self.__total_trips == 0:
            self.__rating = new_rating
        else:
            self.__rating = (
                (self.__rating * self.__total_trips + new_rating)
                / (self.__total_trips + 1)
            )

        self.__total_trips += 1

    def get_rating_info(self):
        return (
            f"Driver rating: {self.__rating:.2f}/5.0 | "
            f"Total trips: {self.__total_trips}"
        )


print("===== PASSENGER =====")

passenger = PassengerAccount("Juan")
passenger.top_up_wallet(500)
passenger.pay_for_ride(150)


print("\n===== DRIVER =====")

driver = DriverAccount("Pedro", "ABC-1234")
driver.add_rating(4.0)
driver.add_rating(5.0)
driver.add_rating(3.0)

print(driver.get_rating_info())

