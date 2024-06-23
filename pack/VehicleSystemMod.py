class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Category: {self.category}"


class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []
        self.vehicle_set = set()
        self.categorized_vehicles = {}

    def add_vehicle(self, vehicle):
        if vehicle.vehicle_id not in self.vehicle_set:
            self.vehicles.append(vehicle)
            self.vehicle_set.add(vehicle.vehicle_id)
            print(f"Vehicle {vehicle.vehicle_id} added successfully!")
        else:
            print("Vehicle already exists in the system!")

    def remove_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                self.vehicle_set.remove(vehicle_id)
                print(f"Vehicle {vehicle_id} removed successfully!")
                return
        print("Vehicle not found in the system!")

    def search_vehicles(self, search_term):
        results = [vehicle for vehicle in self.vehicles if search_term in vehicle.make or search_term in vehicle.model]
        return results

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def categorize_vehicles(self):
        self.categorized_vehicles = {}
        for vehicle in self.vehicles:
            if vehicle.category not in self.categorized_vehicles:
                self.categorized_vehicles[vehicle.category] = [vehicle]
            else:
                self.categorized_vehicles[vehicle.category].append(vehicle)

        for category, vehicles in self.categorized_vehicles.items():
            print(f"Category: {category}")
            for vehicle in vehicles:
                print(vehicle)
            print()
        