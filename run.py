class Bus:
    """
    Bus class to manage passengers and perform bus-related operations.
    """
    def __init__(self):
        """Initialize the Bus object."""
        self.passengers = []  # List to store passenger details
        self.number_of_passengers = 0  # Initialize the count of passengers

    def run(self):
        """Run the bus management system."""
        while True:
            # Display available actions
            print("\n1. Add passengers")
            print("2. Who is on the bus right now?")
            print("3. Calculate total age of passengers")
            print("4. Calculate average age of passengers")
            print("5. Highest age on the bus")
            print("6. Sort bus")
            print("7. How many per gender")
            print("8. Poke a passenger")
            print("9. Remove a passenger")
            print("10. Exit the program")

            choice = input("\nChoose an action: ")
            # Perform actions based on user's choice

            if choice == "1":
                self.add_passenger()
            elif choice == "2":
                self.print_bus()
            elif choice == "3":
                self.calc_total_age()
            elif choice == "4":
                self.calc_average_age()
            elif choice == "5":
                self.max_age()
            elif choice == "6":
                self.sort_bus()
                print("The bus has been sorted by age.")
            elif choice == "7":
                self.print_sex()
            elif choice == "8":
                while True:
                    try:
                        position = int(input(
                                "In which seat number do you"
                                " want to poke the person?: "))
                        break
                    except ValueError:
                        print("Incorrect input. Please input a number.")
                self.poke(position)
            elif choice == "9":
                while True:
                    try:
                        position = int(input(
                            "From which seat number would you like "
                            "to remove the person and remove from the bus?: "))

                        break
                    except ValueError:
                        print("Incorrect input. Please input a number.")

                self.getting_off(position)
            elif choice == "10":
                print("Program will now exit")
                break
            else:
                print("Incorrect input. Try again")

    def add_passenger(self):
        """Add a new passenger to the bus."""
        if self.number_of_passengers < 25:  # Check if the bus is not full
            while True:
                """ Input passenger details: age and gender"""
                try:
                    age = int(input("Input passengers age: "))

                    if age >= 0:
                        break
                    else:
                        print("The age has to be a positive number.")
                except ValueError:
                    print(
                        "Incorrect input. Please input"
                        " a number that represents your age")

            while True:
                gender = input(
                    "Please input the passengers gender (m/f): ").lower()

                if gender == "m" or gender == "f":
                    break
                else:
                    print("Incorrect input. Please input either 'm' or 'f'.")
            self.passengers.append({"age": age, "gender": gender})
            self.number_of_passengers += 1
            print("Passenger added.")
        else:
            print(
                "Bus is full. Cannot add more passengers, take the next one!")

    def print_bus(self):
        """Prints the bus and it's passengers"""
        print("\nPassengers in the bus: ")
        for i, passengers in enumerate(self.passengers):
            print(
                f"Seat {i + 1}: Age {passengers['age']}, "
                f"Gender {passengers['gender']}")

    def calc_total_age(self):
        """Calculates total age of passengers"""
        calc_total_age = sum(
            passengers["age"]for passengers in self.passengers)
        print(f"\nTotal age of all passengers: {calc_total_age}")

    def calc_average_age(self):
        if not self.passengers:
            print("\nNo passengers on the bus.")
            return

        total_age = sum(passengers["age"] for passengers in self.passengers)
        average_age = total_age / len(self.passengers)
        print(f"\nAverage age on the bus: {average_age}.")

    def max_age(self):
        if not self.passengers:
            print("\nNo passengers on the bus. ")
            return

        max_passenger = max(self.passengers, key=lambda x: x["age"])
        print(
            f"\nOldest passengers age: Age {max_passenger['age']}, "
            f"Gender {max_passenger['gender']}")

    def find_age(self, min_age, max_age):
        matching_passengers = [
            passengers for passengers in self.passengers
            if min_age <= passengers["age"] <= max_age]
        if matching_passengers:
            print(f"\nPassengers with age between {min_age} and {max_age}:")
            for i, passengers in enumerate(matching_passengers):
                print(
                    f"\nSeat {i + 1}: Age {passengers['age']}, "
                    f"Gender {passengers['gender']}")
        else:
            print(
                f"\nNo passengers between the age of {min_age} "
                f"and {max_age} found on the bus.")

    def sort_bus(self):
        self.passengers.sort(key=lambda x: x["age"], reverse=True)

    def print_sex(self):
        male_passengers = [
            passengers for passengers in self.passengers
            if passengers['gender'] == 'm']
        female_passengers = [
            passengers for passengers in self.passengers
            if passengers['gender'] == 'f']

        print("\nMale Passengers: ")
        for i, passengers in enumerate(male_passengers):
            print(f"Seat {i + 1}: Age {passengers['age']}")

        print("\nFemale Passengers: ")
        for i, passengers in enumerate(female_passengers):
            print(f"Seat {i + 1}: Age {passengers['age']}")

    def poke(self, position):
        if 1 <= position < len(self.passengers) + 1:
            passenger = self.passengers[position - 1]
            if passenger['gender'] == 'm':
                print(
                    f"You are poking a male passenger "
                    f"with the age {passenger['age']}.")
            else:
                print(
                    f"You are poking a female passenger "
                    f"with the age {passenger['age']}.")
            print("The person has been poked.")
        else:
            print("Empty seat, try again!")

    def getting_off(self, position):
        if 1 <= position < len(self.passengers) + 1:
            self.passengers.pop(position - 1)
            self.number_of_passengers -= 1
            print(f"Passengers on seat {position} has left the bus.")
        else:
            print("Empty seat. try again!")


class Program:
    """
    Program class to initialize and run the bus management system.
    """
    def __init__(self):
        """Initialize the Program object."""
        self.mybus = Bus()

    def run(self):
        """Run the program."""
        self.mybus.run()


if __name__ == "__main__":
    """Create an instance of Program class and run the program"""
    my_program = Program()
    my_program.run()
