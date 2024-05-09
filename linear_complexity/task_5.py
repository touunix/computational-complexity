"""
In the array of integers, rearrange the numbers so that first there are
only negative numbers, and then positive ones
Hint: follow the two indices from left to right. The left indicates a positive number,
the right one a negative number. Swap these numbers places, increase both indexes by 1, the right index
looks for the next negative number (the left one is already pointing to a positive number, because it was skipped by
the right index - it is only interested in negative numbers)
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def segregate_positive_negative(array: list) -> list:
        left_index: int = 0
        right_index: int = 0

        while right_index < len(array):
            if array[right_index] < 0:  # check if number is negative
                array[left_index], array[right_index] = array[right_index], array[left_index]  # swap numbers
                left_index += 1
            right_index += 1
        return array


if __name__ == "__main__":
    input_array: list = Generator.generate_input_negative_positive_array()
    sorted_array: list = Program.segregate_positive_negative(input_array)

    print(60 * "-")
    print(f"The result of the sorted array: {sorted_array}")
    print(60 * "-")
