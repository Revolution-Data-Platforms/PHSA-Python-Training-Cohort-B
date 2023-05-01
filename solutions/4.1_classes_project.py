class Car:
    def __init__(self, name):
        self.name = name
        self.is_rented = False

    def rent(self):
        if self.is_rented:
            print(f"{self.name} is already rented.")
        else:
            self.is_rented = True
            print(f"Rented car: {self.name}.")

    def return_car(self):
        if self.is_rented:
            self.is_rented = False
            print("Car returned. Thank you for renting from us!")
        else:
            print(f"{self.name} is not currently rented.")

car1 = Car("Toyota Corolla")
car2 = Car("Honda Civic")
car3 = Car("Mazda3")
cars = [car1, car2, car3]

print("Car Rental System\n")

while True:
    print("Available cars:")
    for i, car in enumerate(cars):
        if not car.is_rented:
            print(f"{i+1}. {car.name}")
    choice = input("\nChoose a car to rent (1/2/3), or enter 0 to exit: ")
    if choice == '0':
        break
    elif choice in ['1', '2', '3']:
        car = cars[int(choice)-1]
        car.rent()
        print("\nAvailable cars:")
        for i, car in enumerate(cars):
            if not car.is_rented:
                print(f"{i+1}. {car.name}")
        choice = input("\nReturn the rented car (y/n)? ")
        if choice.lower() == 'y':
            car.return_car()
    else:
        print("Invalid input.")
