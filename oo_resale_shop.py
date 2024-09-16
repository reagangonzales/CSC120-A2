
from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory: dict[int, Computer] = {}

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = inventory

    # What methods will you need?
    def buy(self, computer: Computer):
        """
        Adds a new computer to the inventory and returns the assigned item ID.
        """
        self.itemID += 1  
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
            for item_id in self.inventory:
                print(f'Item ID: {item_id} : {self.description}')
        else:
            print("No inventory to display.")
        
    def refurbish(self, item_id: int, new_os: [str] = None):
        """
        Updates the price based on the age of the computer and optionally updates the OS.
        """
        if self.year_made < 2000:
            self.price = 0  
        elif self.year_made < 2012:
            self.price = 250  
        elif self.year_made < 2018:
            self.price = 550 
        else:
            self.price = 1000  

        if new_os is not None:
            self.operating_system = new_os  # Update details after installing new OS

# Create our computers to get our two classes to interact
c1 = Computer("2019 Macbook Pro",
              "Intel", 256, 16,
              "High Sierra", 2019, 1000)
c2 = Computer("HP",
              "OS", 256, 16,
              "High Sierra", 2015, 2000)
c3 = Computer("iPad",
              "OS", 256, 16,
              "High Sierra", 2000, 3000)

def main():  
    # Create a new resale shop
    shop = ResaleShop([c1, c2])

    # Create a computer and add it to the shop
    computer = Computer(description="2019 MacBook Pro", processor_type="Intel", 
                        hard_drive_capacity=256, memory=16, 
                        operating_system="High Sierra", year_made=2019, price=1000)
    item_id = shop.buy(computer)

    # Print the current inventory
    shop.print_inventory()

    # Refurbish the computer and update the OS
    shop.refurbish(item_id, new_os="Ventura")
    
    # Print the updated inventory
    shop.print_inventory()
          
main()
    


