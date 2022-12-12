import numpy as np
import re

DIR_LETTERS = {
    'R': np.array([1, 0]),
    'D': np.array([0, -1]),
    'L': np.array([-1, 0]),
    'U': np.array([0, 1]),
}

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').readlines()
    head = np.array([0, 0])
    tail = np.array([0, 0])
    visited_pos = set()
    for line in lines:
        move, n = re.search(r"(.+) (\d+)", line.strip()).groups()
        n = int(n)
        for i in range(n):
            visited_pos.add(str(tail))
            head = head + DIR_LETTERS[move]
            offset = head - tail
            manhattan_dist = abs(offset[0]) + abs(offset[1])
            offset_one = np.sign(offset)
            while manhattan_dist > abs(offset_one[0]) + abs(offset_one[1]):
                tail = tail + offset_one
                manhattan_dist -= abs(offset_one[0]) + abs(offset_one[1])
    visited_pos.add((str(tail)))
    print("Answer 1:", len(visited_pos))

    chain = [np.array([0, 0]) for i in range(10)]
    visited_pos = set()
    for line in lines:
        move, n = re.search(r"(.+) (\d+)", line.strip()).groups()
        n = int(n)
        for i in range(n):
            visited_pos.add(str(chain[-1]))
            chain[0] = chain[0] + DIR_LETTERS[move]
            for c in range(9):
                offset = chain[c] - chain[c + 1]
                manhattan_dist = abs(offset[0]) + abs(offset[1])
                offset_one = np.sign(offset)
                while manhattan_dist > abs(offset_one[0]) + abs(offset_one[1]):
                    chain[c + 1] = chain[c + 1] + offset_one
                    manhattan_dist -= abs(offset_one[0]) + abs(offset_one[1])
    visited_pos.add((str(chain[-1])))
    print("Answer 2:", len(visited_pos))
