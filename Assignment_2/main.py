import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True
    while is_on:
        choice = input("Would you like to S/M/L: ").lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print("Resources Left:")
            for item, amount in resources.items():
                print(f"{item}: {amount}")
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.transaction_result(choice, sandwich["ingredients"])
        else:
            print("Invalid choice.")





if __name__=="__main__":
    main()