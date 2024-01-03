class Bus:
    def __init__(self):
        self.passengers = []
        self.number_of_passengers = 0
    
    def run(self):
        while True:
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
                        position = int(input("In which seat number do you want to poke the person?: "))
                        break
                    except ValueError:
                        print("Incorrect input. Please input a number.")
                    self.poke(position)
                elif choice == "9":
                    while True:
                        try:
                            position = int(input("From which seat number would you like to remove the person and remove from the bus?: "))
                            break
                        except ValueError:
                            print("Incorrect input. Please input a number.")
                    
                    self.getting_off(position)
                elif choice == "10":
                    print("Program will now exit")
                    break
                else:
                    print("Incorrect input. Try again")
                    