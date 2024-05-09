"""
The input is the number k. As in Task 1, only we are looking for the number
closest to the number k (and the position at which it occurs). If the array
contains k, then this number is the solution.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def find_nearest_number(search_number: int, array: list) -> tuple[int, [int | None]]:
        nearest_number: [int | None] = None
        min_difference: [int | float] = float("inf")  # initial value for difference
        position: int = -1

        for number in array:
            difference: int = abs(number - search_number)
            if difference < min_difference:
                min_difference: [int | float] = difference
                nearest_number: [int | None] = number
                position: int = array.index(number)
        return position, nearest_number


if __name__ == "__main__":
    input_search_number: int = Generator.generate_random_search_number()
    input_array: list = Generator.generate_input_array()
    output_position, output_nearest = Program.find_nearest_number(input_search_number, input_array)

    print(60 * "-")
    print(f"Generated random input search number: {input_search_number}")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")
    print(f"Position of the number nearest to {input_search_number} in the table: {output_position}")
    print(f"The closest number to {input_search_number} in the table: {output_nearest}")
    print(60 * "-")
