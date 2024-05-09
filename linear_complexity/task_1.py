"""
Write a program that receives a number on input and returns the position in the array,
on which this number occurs. If the number is not in the array, return -1
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def find_number(search_number: int, array: list) -> int:
        for number in array:
            if number == search_number:
                return array.index(number)
        return -1


if __name__ == "__main__":
    input_search_number: int = Generator.generate_random_search_number()
    input_array: list = Generator.generate_input_array()
    position = Program.find_number(input_search_number, input_array)

    print(60 * "-")
    print(f"Generated random input search number: {input_search_number}")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")
    print(f"Position of number {input_search_number} in the array: {position}")
    print(60 * "-")
