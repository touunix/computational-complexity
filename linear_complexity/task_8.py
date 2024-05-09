"""
Check that the whole input board is one big peak. Calculate its height.
"""
from utilities.generator import Generator


class Program:
    @staticmethod
    def is_single_peak(array: list) -> tuple[bool, None] | tuple[bool, int]:
        total_length: int = len(array)
        if total_length < 3:
            return False, None  # array must contain at least 3 elements to be a peak

        index: int = 1
        while index < total_length and array[index] > array[index - 1]:  # rising slope
            index += 1

        if index == total_length:  # check if there are some decreasing parts to consider as a peak
            return False, None

        while index < total_length and array[index] < array[index - 1]:  # slope
            index += 1

        if index != total_length:
            return False, None  # there are numbers greater than the maximum

        height: int = max(array) - min(array)
        return True, height


if __name__ == "__main__":
    peak_top_height: int = Generator.generate_peak_top_height()
    input_array: list = [1, 2, 3, peak_top_height, 3, 2, 1]
    is_peak, peak_height = Program.is_single_peak(input_array)

    print(60 * "-")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")

    if is_peak:
        print("The array constitutes a single peak.")
        print(f"The height of the peak is: {peak_height}")
    else:
        print("The array does not constitute a single peak.")
    print(60 * "-")
