class TimeMap:

    def __init__(self):
        self.container = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.container.keys():
            self.container[key] = [(value, timestamp)]
        else:
            self.container[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.container.keys():
            return ""
        value_timestamp_list = self.container[key]
        if value_timestamp_list[0][1] > timestamp:
            return ""

        left, right = 0, len(value_timestamp_list) - 1
        mid = (left + right) // 2
        while left <= right:
            if value_timestamp_list[mid][1] == timestamp:
                return value_timestamp_list[mid][0]
            elif value_timestamp_list[mid][1] < timestamp:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return value_timestamp_list[right][0]   