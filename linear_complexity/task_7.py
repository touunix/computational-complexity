"""
Find the hill with the widest base (not necessarily the highest). Warning:
a hill can also have only one wall and then a fault, e.g.
[3, 6, 1, 5, 7, 8, 4, 3, 2, 6, 7, 1, 5, 9]
"""


class Program:
    @staticmethod
    def find_widest_peak(array: list) -> list:
        max_width: int = 0
        peak_start: int = 0
        peak_end: int = 0

        index: int = 1
        total_length: int = len(array) - 1

        while index < total_length:
            if array[index] > array[index - 1] and array[index] > array[index + 1]:
                start: int = index  # peak starts
                while index < total_length and array[index] > array[index + 1]:
                    index += 1  # peak continues increasing
                end: int = index  # peaks ends
                width: int = end - start + 1  # calculate peak width

                if width > max_width:
                    max_width: int = width
                    peak_start: int = start
                    peak_end: int = end
            else:
                index += 1  # indicate that it is not a peak

        return array[peak_start:peak_end + 1]


if __name__ == "__main__":
    input_array: list = [3, 6, 1, 5, 7, 8, 4, 3, 2, 6, 7, 1, 5, 9]
    widest_peak: list = Program.find_widest_peak(input_array)

    print(60 * "-")
    print(f"Generated random input array: {input_array}")
    print(60 * "-")
    print(f"The widest peak is: {widest_peak}")
    print(60 * "-")
