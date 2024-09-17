from typing import Dict, Optional

class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: str,
                    memory: str,
                    operating_system: str,
                    year_made: str,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
    # What methods will you need?

    # Method to display computer's information
    def __str__(self) -> str:
        return (f"""Description: {self.description} 
Processor: {self.processor_type}
HD Capacity: {self.hard_drive_capacity}GB 
Memory: {self.memory}GB 
OS: {self.operating_system} 
Year Made: {self.year_made}
Price: ${self.price}""")
    
    # Method to get the description of the computer
    def get_description(self) -> str:
        return self.description

    # Method to get the processor type of the computer
    def get_processor_type(self) -> str:
        return self.processor_type

    # Method to get the hard drive capacity of the computer
    def get_hard_drive_capacity(self) -> int:
        return self.hard_drive_capacity

    # Method to get the memory of the computer
    def get_memory(self) -> int:
        return self.memory

    # Method to get the operating system of the computer
    def get_operating_system(self) -> str:
        return self.operating_system

    # Method to get the year the computer was made
    def get_year_made(self) -> int:
        return self.year_made

    # Method to get the price of the computer
    def get_price(self) -> int:
        return self.price   


def main():

    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    # Testing methods
    print(my_computer)
    print(my_computer.get_description())
    print(my_computer.get_hard_drive_capacity())
    print(my_computer.get_memory())
    print(my_computer.get_operating_system())
    print(my_computer.get_price())
    print(my_computer.get_processor_type())
    print(my_computer.get_year_made())
    


main()
