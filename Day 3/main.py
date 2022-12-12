import itertools

DEBUG = True

def letter_to_priority(c):
    if c == c.lower():
        return ord(c) - 96
    if c == c.upper():
        return ord(c) - 64 + 26

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').readlines()

    total_score = 0
    for line in lines:
        line = line.strip()
        if DEBUG:
            print(len(line), line)
        comp_a = line[:round(len(line) / 2)]
        comp_b = line[round(len(line) / 2):]
        shared = [c for c in comp_a if c in comp_b][0]
        print(comp_a, comp_b, shared)
        letter_priority = letter_to_priority(shared)
        print(letter_priority)
        total_score += letter_priority
    print('Answer 1:', total_score)

    total_score = 0
    for i in range(0, len(lines), 3):
        group = lines[i:i + 3]
        group = [line.strip() for line in group]
        shared = [c for c in group[0] if c in group[1] and c in group[2]][0]
        total_score += letter_to_priority(shared)
    print('Answer 2:', total_score)
