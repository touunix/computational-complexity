"""
Given an array sorted in ascending order and a number k, check that it occurs in
this array using the half method: first check if the middle element of
the array = k. If it is smaller than k then continue in the same way looking for k in the
right half of the array; if it is smaller, then in the left half.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def binary_search(search_number: int, array: list) -> bool:
        left_pointer: int = 0
        right_pointer: int = len(array) - 1

        while left_pointer <= right_pointer:
            mid: int = (left_pointer + right_pointer) // 2
            if array[mid] == search_number:  # look in the middle
                return True
            elif array[mid] < search_number:  # look in the left
                left_pointer: int = mid + 1
            else:
                right_pointer: int = mid - 1  # look in the right
        return False


if __name__ == "__main__":
    input_array: list = Generator.generate_ascending_array()
    input_search_number: int = Generator.generate_random_search_number()

    print(60 * "-")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")

    if Program.binary_search(input_search_number, input_array):
        print(f"The number: {input_search_number}, is in the array.")
    else:
        print(f"The number: {input_search_number}, is not in the array.")
    print(60 * "-")
