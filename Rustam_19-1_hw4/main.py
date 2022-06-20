from cars.create_car import Car
from cars.get_car_info import get_car_info

car = Car("Mercedes", "S500", "Black")
get_car_info(car)
car.start_engine()
car.stop_engine()
