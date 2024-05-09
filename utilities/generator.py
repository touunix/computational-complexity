import random


class Generator:
    @staticmethod
    def generate_input_array() -> list:
        array_length: int = random.randint(a=1, b=30)
        return [random.randint(a=0, b=50) for _ in range(array_length)]

    @staticmethod
    def generate_input_negative_positive_array() -> list:
        array_length: int = random.randint(a=1, b=30)
        return [random.randint(a=-25, b=25) for _ in range(array_length)]

    @staticmethod
    def generate_random_search_number() -> int:
        return random.randint(a=0, b=50)

    @staticmethod
    def generate_ascending_array() -> list:
        array_length: int = random.randint(a=1, b=30)
        return sorted([random.randint(a=0, b=50) for _ in range(array_length)])

    @staticmethod
    def generate_peak_top_height() -> int:
        return random.randint(a=0, b=25)
