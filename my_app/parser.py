def parse_input(input_str):
    result = {}
    pairs = input_str.split(",")
    for pair in pairs:
        name, value = pair.split(":")
        result[name.strip()] = int(value.strip())
    return result


def total_amount(data):
    return sum(data.values())


def max_person(data):
    return max(data, key=data.get)


def min_person(data):
    return min(data, key=data.get)
