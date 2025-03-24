class Vehicle:
    def __init__(self, name, year, max_speed, mileage, colour):
        # Check if inputs are valid
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Max speed must be a number")
        if not isinstance(mileage, (int, float)):
            raise TypeError("Mileage must be a number")
        if not isinstance(colour, str):
            raise TypeError("Colour must be a string")
        
        # Set basic vehicle info
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour
    
    def print_details(self):
        # Print all vehicle info
        print(f"\nVehicle Details:")
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Mileage: {self.mileage}")
        print(f"Colour: {self.colour}")
    
    # Update methods
    def update_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.name = new_name
    
    def update_year(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError("Year must be an integer")
        self.year = new_year
    
    def update_max_speed(self, new_max_speed):
        if not isinstance(new_max_speed, (int, float)):
            raise TypeError("Max speed must be a number")
        self.max_speed = new_max_speed
    
    def update_mileage(self, new_mileage):
        if not isinstance(new_mileage, (int, float)):
            raise TypeError("Mileage must be a number")
        self.mileage = new_mileage
    
    def update_colour(self, new_colour):
        if not isinstance(new_colour, str):
            raise TypeError("Colour must be a string")
        self.colour = new_colour

class ElectricVehicle(Vehicle):
    def __init__(self, name, year, max_speed, mileage, colour, battery_capacity, range):
        # Set up basic vehicle attributes
        super().__init__(name, year, max_speed, mileage, colour)
        
        # Check EV-specific inputs
        if not isinstance(battery_capacity, (int, float)):
            raise TypeError("Battery capacity must be a number")
        if not isinstance(range, (int, float)):
            raise TypeError("Range must be a number")
            
        self.battery_capacity = battery_capacity  # kWh
        self.range = range  # km
    
    def print_details(self):
        # Print all details including EV-specific ones
        super().print_details()
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Range: {self.range} km")
    
    def update_battery_capacity(self, new_capacity):
        if not isinstance(new_capacity, (int, float)):
            raise TypeError("Battery capacity must be a number")
        self.battery_capacity = new_capacity
    
    def update_range(self, new_range):
        if not isinstance(new_range, (int, float)):
            raise TypeError("Range must be a number")
        self.range = new_range

def main():
    # Test examples
    my_car = Vehicle("Bugatti", 2025, 300, 50000, "Blue")
    my_ev = ElectricVehicle("Tesla Model X", 2022, 200, 69000, "Black", 75, 400)
    
    print("\nInitial Details ")
    my_car.print_details()
    my_ev.print_details()
    
    # update methods for Vehicle
    print("\n Updating Vehicle Details")
    my_car.update_colour("Black")
    my_car.update_mileage(55000)
    my_car.print_details()
    
    # update methods for Ev
    print("\nUpdating Electric Vehicle Details")
    my_ev.update_battery_capacity(50)
    my_ev.update_range(450)
    my_ev.print_details()

if __name__ == "__main__":
    main() 