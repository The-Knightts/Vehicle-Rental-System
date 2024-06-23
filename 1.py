from pack.VehicleSystemMod import *

Car = VehicleRentalSystem()

while True:
    print("\nVehicle Rental System Menu:")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Search Vehicles")
    print("4. List All Vehicles")
    print("5. Display Categorized Vehicles")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vehicle_id = input("Enter vehicle ID: ")
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        year = input("Enter vehicle year: ")
        category = input("Enter vehicle category: ")
        vehicle = Vehicle(vehicle_id, make, model, year, category)
        Car.add_vehicle(vehicle)

    elif choice == 2:
        vehicle_id = input("Enter vehicle ID to remove: ")
        Car.remove_vehicle(vehicle_id)

    elif choice == 3:
        search_term = input("Enter the model or the make: ")
        results = Car.search_vehicles(search_term)
        if results:
            print("Search results:")
            for vehicle in results:
                print(vehicle)
        else:
            print("No vehicles found!")

    elif choice == 4:
        Car.list_vehicles()

    elif choice == 5:
        Car.categorize_vehicles()

    elif choice == 6:
        print("Exiting the system. Bye bye!")
        
    else:
        print("Invalid choice. Enter a Valid Choice and Please try again!")
