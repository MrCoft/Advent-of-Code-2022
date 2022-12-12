import re

def overlaps_completely(a, b, c, d):
    return (c >= a and d <= b) or (a >= c and b <= d)

def overlaps_partially(a, b, c, d):
    # return (c <= b and d >= a) or (a <= d and b >= c) FIXED
    return any(i in range(c, d + 1) for i in range(a, b + 1))

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').readlines()
    total_complete = 0
    total_partial = 0
    for line in lines:
        a, b, c, d = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()
        a, b, c, d = map(lambda s: int(s), [a, b, c, d])
        if overlaps_completely(a, b, c, d):
            total_complete += 1
        if overlaps_partially(a, b, c, d):
            total_partial += 1
    print("Answer 1:", total_complete)
    print("Answer 2:", total_partial)
