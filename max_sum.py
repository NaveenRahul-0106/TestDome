def find_max_sum(numbers):
    m1 = max(numbers)
    numbers.remove(m1)
    m2 = max(numbers)
    return m1+ m2

if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))


def find_max_sum(numbers):
    return sum(sorted(numbers)[-2:])

if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))
