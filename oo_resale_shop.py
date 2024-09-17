# Useful containers from the typing module
from computer import Computer
from typing import Dict, Optional

class ResaleShop:

    # What attributes will it need?
    inventory: dict[int, Computer] = {}
    itemID: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list, itemID: int):
        self.inventory = inventory
        self.itemID = itemID

    # What methods will you need?
    def buy(self, computer: Computer) -> int:
        """
        Adds a new computer to the inventory and returns the assigned item ID.
        """
        self.itemID += 1  # Increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    def update_price(self, item_id: int, new_price: int):
        """
        Updates the price of a computer in the inventory based on its ID.
        """
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price
        else:
            print(f"Item {item_id} not found. Cannot update price.")

    def sell(self, item_id: int):
        """
        Removes a computer from the inventory based on its item ID.
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    def print_inventory(self):
        """
        Prints details of all computers in the inventory.
        """
        if self.inventory:
            for item_id, computer in self.inventory.items():
                print(f'Item ID: {item_id} : {computer}')
        else:
            print("No inventory to display.")

    def refurbish(self, new_os: Optional[str] = None):
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000

        if new_os is not None:
            self.operating_system = new_os

def main():
    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    # Create a new resale shop
    shop = ResaleShop(my_computer, 1)

    # Create and add a computer to the shop
    computer1 = Computer(
        description="2019 MacBook Pro",
        processor_type="Intel",
        hard_drive_capacity=256,
        memory=16,
        operating_system="High Sierra",
        year_made=2019,
        price=1000
    )
    shop.buy(computer1)

    # Create and add another computer to the shop
    computer2 = Computer(
        description="2015 Dell XPS 13",
        processor_type="Intel",
        hard_drive_capacity=512,
        memory=8,
        operating_system="Windows 10",
        year_made=2015,
        price=800
    )
    shop.buy(computer2)

    # Print the current inventory
    shop.print_inventory()

    # Refurbish the first computer and update the OS
    shop.refurbish(1, new_os="Ventura")
    
    # Print the updated inventory
    shop.print_inventory()

main()
    