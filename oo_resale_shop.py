# Useful containers from the typing module
from computer import Computer
from typing import Dict, Optional

class ResaleShop:

    # What attributes will it need?
    inventory: dict[int, Computer] = {}
    item_ID: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory: Dict[int, Computer] = {}
        self.item_id = 0

    # What methods will you need?
    # Buy method
    def buy(self, computer: Computer) -> int:
        self.item_id += 1  # increment itemID
        self.inventory[self.item_id] = computer
        return self.item_id

    # Update price method
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price
        else:
            print(f"Item {item_id} not found. Cannot update price.")

    # Sell method
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    # Print inventory method
    def print_inventory(self):
        if self.inventory:
            for item_id, computer in self.inventory.items():
                print(f"Item ID: {item_id} : {computer}")
        else:
            print("No inventory to display.")

    # Refurbish method
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            # Refurbish the computer based on its year
            if computer.year_made < 2000:
                computer.price = 0  
            elif computer.year_made < 2012:
                computer.price = 250  
            elif computer.year_made < 2018:
                computer.price = 550 
            else:
                computer.price = 1000 

            # Update operating system if provided
            if new_os is not None:
                computer.operating_system = new_os
        else:
            print(f"Item {item_id} not found. Please select another item to refurbish.")


def main():
    shop = ResaleShop()

    # Add computers to the shop's inventory
    computer1 = shop.buy(Computer(description="2019 MacBook Pro", processor_type="Intel",
                              hard_drive_capacity=256, memory=16, operating_system="High Sierra",
                              year_made=2019, price=1000))
    
    computer2 = shop.buy(Computer(description="2010 Dell XPS", processor_type="Intel",
                              hard_drive_capacity=500, memory=8, operating_system="Windows 10",
                              year_made=2010, price=600))

    computer3 = shop.buy(Computer(description="2005 HP Pavilion", processor_type="AMD",
                              hard_drive_capacity=250, memory=4, operating_system="Windows XP",
                              year_made=2005, price=150))

    # Print the inventory
    print("Initial Inventory:")
    shop.print_inventory()
    print()

    # Update the price of computer 2
    shop.update_price(item_id=computer2, new_price=500)

    # Refurbish the computers
    shop.refurbish(item_id=computer3, new_os="Linux")
    shop.refurbish(item_id=computer1)
    shop.refurbish(item_id=computer2)

    # Print the inventory to see the updated prices and refurbishing
    print("Inventory after updating price and refurbishing:")
    shop.print_inventory()
    print()

    # Sell the first item
    shop.sell(item_id=computer1)

    # Print the inventory to see the changes after selling an item
    print("Final Inventory:")
    shop.print_inventory()


main()
    