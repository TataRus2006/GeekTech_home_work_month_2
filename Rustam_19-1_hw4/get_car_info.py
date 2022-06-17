from .create_car import Car

class Get_Car_Info(Car):
    def info(self):
        print(f"""
        Title: {self.title}
        Model: {self.model}
        Color: {self.color}
        """)

# mers = Get_Car_Info(title="Mercedes", model="S500", color="Black")
# mers.info()
# mers.start_engine()
# mers.stop_engine()
