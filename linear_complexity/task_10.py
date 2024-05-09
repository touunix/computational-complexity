"""
Given a number k as an input, check whether there exists in the array of positive numbers its
fragment (from to) with sum = k. (Use a "snake", viz: 2 indexes crawling from
left to right: if tab[i] + tab[i+1] + ... + tab[j] < k, then j++, and if < k, then i++
"""


class Program:
    @staticmethod
    def find_subarray_sum(search_sum: int, array: list) -> bool:
        total_length: int = len(array)
        left_index: int = 0
        right_index: int = 0
        current_sum: int = array[0]

        while right_index < total_length:
            if current_sum == search_sum:
                return True
            elif current_sum < search_sum:
                right_index += 1
                if right_index < total_length:
                    current_sum += array[right_index]
            else:
                current_sum -= array[left_index]
                left_index += 1
        return False


if __name__ == "__main__":
    input_array: list = [1, 4, 2, 2, 8, 1]
    input_sum: int = 11

    print(60 * "-")
    print(f"Input array: {input_array}")
    print(60 * "-")

    if Program.find_subarray_sum(input_sum, input_array):
        print(f"Fragment was found with the sum of: {input_sum}")
    else:
        print(f"Fragment with sum: {input_sum} not found")
    print(60 * "-")
