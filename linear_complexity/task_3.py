"""
We have the number k as an input. Look for, in an ascending array, not one, but
two numbers a and b such that a + b = k.
"""

from utilities.generator import Generator


class Program:
    @staticmethod
    def find_two_numbers_sum(search_sum: int, array: list) -> tuple[int, int] | tuple[None, None]:
        left: int = 0  # start index of array
        right: int = len(array) - 1  # end index of array

        while left < right:
            current_sum = array[left] + array[right]
            if current_sum == search_sum:
                return array[left], array[right]
            elif current_sum < search_sum:
                left += 1
            else:
                right -= 1

        return None, None


if __name__ == "__main__":
    input_search_number: int = Generator.generate_random_search_number()
    input_array: list = Generator.generate_ascending_array()
    number_1, number_2 = Program.find_two_numbers_sum(input_search_number, input_array)

    print(60 * "-")
    print(f"Generated random input search number: {input_search_number}")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")

    if number_1 and number_2:
        print(f"Two numbers whose sum is {input_search_number}: {number_1} and {number_2}")
    else:
        print(f"Two numbers whose sum is {input_search_number} are not found in the array")
