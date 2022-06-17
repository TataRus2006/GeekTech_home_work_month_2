class Car:
    def __init__ (self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')

    def stop_engine(self):
        print(f'{self.title} {self.model} engine stopped!')

    def get_info(self):
        print(f"""
Title: {self.title}
Model: {self.model}
Weight: {self.weight} 
Hp: {self.hp} 
Nm: {self.nm} 
Max_speed: {self.max_speed} 
Color: {self.color} 
        """)

BMW = Car("BMW", "i8", "1855 kilograms", 362, 570, "250 km/h", 'white' )
BMW.start_engine()
BMW.stop_engine()
BMW.get_info()

Mercedes = Car("Mercedes-Benz", "300SL", "1560 kilograms",  175, 207, "263 km/h", 'white' )
Mercedes.start_engine()
Mercedes.stop_engine()
Mercedes.get_info()
