"""
Sort an array that is a mountain in ascending order. E.g. [3, 5, 6, 8, 4, 3, 1] ->
[1, 3, 3, 4, 5, 6, 8]. Merge the two sorted slopes into a separate array, similar to the
merging in the mergesort algorithm.
"""


class Program:
    @staticmethod
    def _merge_sorted_arrays(ascending_array: list, descending_array: list) -> list:
        index_ascending: int = 0
        index_descending: int = 0
        merged: list = []

        while index_ascending < len(ascending_array) and index_descending < len(descending_array):
            if ascending_array[index_ascending] < descending_array[index_descending]:
                merged.append(ascending_array[index_ascending])
                index_ascending += 1
            else:
                merged.append(descending_array[index_descending])
                index_descending += 1

        while index_ascending < len(ascending_array):
            merged.append(ascending_array[index_ascending])
            index_ascending += 1

        while index_descending < len(descending_array):
            merged.append(descending_array[index_descending])
            index_descending += 1
        return merged

    def sort_peak_array(self, array: list) -> list:
        peak_top: int = max(array)
        peak_index: int = array.index(peak_top)

        # division of the hill into two sorted slopes
        ascending: list = array[:peak_index + 1]
        descending: list = array[peak_index + 1:][::-1]
        return self._merge_sorted_arrays(ascending, descending)


if __name__ == "__main__":
    program = Program()
    input_array: list = [3, 5, 6, 8, 4, 3, 1]
    sorted_peak: list = program.sort_peak_array(input_array)

    print(60 * "-")
    print(f"Input array: {input_array}")
    print(60 * "-")
    print(f"Sorted peak: {sorted_peak}")
    print(60 * "-")
