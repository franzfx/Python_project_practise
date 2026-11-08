from statistics import mean

expences = []

def main():
    print("\nWellcome back!")
    get_choice()
   
def get_choice():
    valid_choices = ["new", "summary", "expences", "done"]
    
    while True:
    
        choice = input("\nWhat would you like to do today?\n"
                        "(type NEW to enter new expence)\n"
                        "(type SUMMARY to get basic info about your expences)\n"
                        "(type EXPENCES to get a list of your expences)\n"
                        "(type DONE to finish)\n"
        ).lower().strip()

        if choice not in valid_choices:
            print("Type one of the given options above")
            continue

        if choice == "new":
            get_expences()
        elif choice == "summary":
            if not expences:
                print("No expences recorded yet")
            else:
                total, average, largest = expences_summary()
                print(f"\n---SUMMARY---\nTotal: {total:.2f} PLN\nAverage: {average:.2f} PLN\nLargest: {largest:.2f} PLN")
        elif choice == "expences":
            if not expences:
                print("No expences recorded yet")
            else:
                print("\nYour expences:")
                for item in expences:
                    print(f"- {item['name']}: {item['cost']:.2f} PLN")
        else:
            print("See you later!")
            break


def get_expences():
    
    while True:
        name = input("Expence name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            print("See you later!")
            break

        if not name:
            print("Please enter a name of the expence")
            continue

        try:
            cost = float(input("Cost: "))
        except ValueError:
            print("Please enter a valid number for the cost")
            continue

        if cost < 0:
            print("The cost cannot be negative")
            continue

        expences.append({"name": name, "cost": cost})
        print(f"Added {name}: {cost:.2f} PLN\n")


def expences_summary():
    costs = [float(item["cost"]) for item in expences]
    total = sum(costs)
    average = mean(costs) 
    largest = max(costs)

    return total, average, largest


if __name__ == "__main__":
    main()