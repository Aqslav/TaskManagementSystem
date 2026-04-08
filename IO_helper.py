import json


class IO_helper:
    @staticmethod
    def save(data, filename):
        arr = []
        for item in data:
            if hasattr(item, "__dict__"):
                arr.append(item.__dict__)
            elif isinstance(item, dict):
                arr.append(item)
            else:
                raise TypeError(f"Unsupported item type: {type(item).__name__}")

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)