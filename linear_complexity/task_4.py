"""
In the input array, find the longest such coherent fragment (from i to
j) in which the numbers increase. E.g., for the array [10, 9, 2, 5, 6, 7, 101, 18],
the response is 5 (substring [2, 5, 6, 7, 101]).
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def find_longest_increasing_subarray(array: list) -> tuple[list, int]:
        max_length: int = 1
        current_length: int = 1
        max_start_index: int = 0
        max_end_index: int = 0
        current_start_index: int = 0

        for index, number in enumerate(array[1:], start=1):
            if number > array[index - 1]:  # check if the current number is greater than the previous one
                current_length += 1
            else:
                # new steak starts
                if current_length > max_length:  # check if current streak is greater than maximum so far
                    max_length: int = current_length
                    max_start_index: int = current_start_index
                    max_end_index: int = index - 1
                current_length: int = 1  # reset the current streak length
                current_start_index: int = index  # save the start index of current streak

        # check if the last streak was the longest, after all iterations
        if current_length > max_length:
            max_length: int = current_length
            max_start_index: int = current_start_index
            max_end_index: int = len(array) - 1

        longest_subarray: list = array[max_start_index:max_end_index + 1]
        return longest_subarray, max_length


if __name__ == "__main__":
    input_array: list = Generator.generate_input_array()
    subarray, subarray_length = Program.find_longest_increasing_subarray(input_array)

    print(60 * "-")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")
    print(f"The longest growing subarray: {subarray}")
    print(f"Length of the longest growing subarray: {subarray_length}")
    print(60 * "-")
