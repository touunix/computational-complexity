"""
We shall call a peak in an array of integers such a fragment of the array, in which
numbers first increase and then decrease. Calculate how many hills there are in the given array
there are peaks.
"""

from utilities.generator import Generator


class Program:
    @staticmethod
    def count_peaks(array: list) -> int:
        peaks: int = 0
        index: int = 1
        total_length: int = len(array) - 1

        while index < total_length:
            if array[index] > array[index - 1] and array[index] > array[index + 1]:
                # check if previous point is smaller and following point is greater
                peaks += 1  # if yes, it is a peak
                while index < total_length and array[index] > array[index + 1]:  # look for peak ends
                    index += 1
            else:
                index += 1  # indicate that it is not a peak
        return peaks


if __name__ == "__main__":
    input_array: list = Generator.generate_input_array()
    number_of_peaks: int = Program.count_peaks(input_array)

    print(60 * "-")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")
    print(f"The number of peaks is: {number_of_peaks}")
    print(60 * "-")
