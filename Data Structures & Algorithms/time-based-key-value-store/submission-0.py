class TimeMap:

    def __init__(self):
        # key -> список пар (timestamp, value)
        self.dict_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict_values.get(key, [])

        if not values:
            return ""

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            saved_timestamp, saved_value = values[mid]

            if saved_timestamp <= timestamp:
                result = saved_value
                left = mid + 1
            else:
                right = mid - 1

        return result
        
