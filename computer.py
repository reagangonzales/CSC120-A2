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
    def __str__(self):
        return (f"Description: {self.description}, Processor: {self.processor_type}, "
                f"HD Capacity: {self.hard_drive_capacity}GB, Memory: {self.memory}GB "
                f"OS: {self.operating_system}, Year Made: {self.year_made}, Price: ${self.price}")
    


def main():
    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    print(my_computer)


main()