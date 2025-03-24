import sys
import os

# Add Part A to Python path so i can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'PartA'))


import unittest
from PartA import Vehicle, ElectricVehicle

class TestVehicleClasses(unittest.TestCase):
    def setUp(self):
        # Create test vehicles
        self.vehicle1 = Vehicle("Toyota Camry", 2020, 180, 50000, "Silver")
        self.vehicle2 = Vehicle("Toyota Camry", 2020, 180, 50000, "Silver")
        self.ev = ElectricVehicle("Tesla Model 3", 2022, 200, 20000, "Red", 75, 400)
    
    def test_instance_checks(self):
        # Check if objects are of the right type
        self.assertIsInstance(self.vehicle1, Vehicle)
        self.assertIsInstance(self.ev, ElectricVehicle)
        self.assertIsInstance(self.ev, Vehicle)  # EV is also a Vehicle
    
    def test_not_instance_checks(self):
        # Check if objects are not of wrong types
        self.assertNotIsInstance(self.vehicle1, ElectricVehicle)
        self.assertNotIsInstance("not a vehicle", Vehicle)
        self.assertNotIsInstance(42, Vehicle)
    
    def test_object_identity(self):
        # Check object identity comparisons
        self.assertIsNot(self.vehicle1, self.vehicle2)  # Different objects
        vehicle3 = self.vehicle1
        self.assertIs(self.vehicle1, vehicle3)  # Same object
    
    def test_update_methods(self):
        # Test regular vehicle updates
        self.vehicle1.update_name("Honda Civic")
        self.assertEqual(self.vehicle1.name, "Honda Civic")
        
        self.vehicle1.update_year(2021)
        self.assertEqual(self.vehicle1.year, 2021)
        
        self.vehicle1.update_max_speed(190)
        self.assertEqual(self.vehicle1.max_speed, 190)
        
        self.vehicle1.update_mileage(55000)
        self.assertEqual(self.vehicle1.mileage, 55000)
        
        self.vehicle1.update_colour("Blue")
        self.assertEqual(self.vehicle1.colour, "Blue")
        
        # Test EV updates
        self.ev.update_battery_capacity(82)
        self.assertEqual(self.ev.battery_capacity, 82)
        
        self.ev.update_range(450)
        self.assertEqual(self.ev.range, 450)
    
    def test_update_type_validation(self):
        # Test error handling for wrong input types
        with self.assertRaises(TypeError):
            self.vehicle1.update_name(123)
            
        with self.assertRaises(TypeError):
            self.vehicle1.update_year("2021")
            
        with self.assertRaises(TypeError):
            self.vehicle1.update_max_speed("fast")
            
        with self.assertRaises(TypeError):
            self.vehicle1.update_mileage("50000")
            
        with self.assertRaises(TypeError):
            self.vehicle1.update_colour(123)
            
        with self.assertRaises(TypeError):
            self.ev.update_battery_capacity("75")
            
        with self.assertRaises(TypeError):
            self.ev.update_range("400")

def main():
    # Run all tests using the unittest framework which will run all thefunctions
    unittest.main(argv=[''], exit=False)

if __name__ == '__main__':
    main() 