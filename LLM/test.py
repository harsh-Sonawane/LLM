
# sample_test.py

from typing import List, Dict, Any

def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

def process_data(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Processes a list of dictionaries and returns a summary."""
    result = {}
    for item in data:
        for key, value in item.items():
            if key not in result:
                result[key] = 0
            if isinstance(value, int):
                result[key] += value
    return result

class Person:
    """Represents a person with a name and age."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

def main():
    """Main function to test the functions and class."""
    print(greet("Alice"))
    print(add_numbers(5, 7))
    
    data = [
        {"item1": 10, "item2": 20},
        {"item1": 5, "item2": 15},
    ]
    print(process_data(data))
    
    person = Person("Bob", 30)
    print(person)

if __name__ == "__main__":
    main()

add_numbers()
