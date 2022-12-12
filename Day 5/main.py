import re
import copy

if __name__ == '__main__':
    crates_init = open('crates_init.txt', encoding='utf-8').readlines()
    stack_index = [crates_init[-1].index(str(i)) for i in range(1, 10)]
    stacks_vertical = [[line[index] if index < len(line) else ' ' for index in stack_index] for line in crates_init[:-1]]
    stacks_raw = [[stacks_vertical[j][i] for j in range(len(stacks_vertical))] for i in range(len(stack_index))]
    stacks = [list(reversed(list(filter(lambda x: x != ' ', stack)))) for stack in stacks_raw]
    stacks_copy = copy.deepcopy(stacks)

    lines = open('input.txt', encoding='utf-8').readlines()
    for line in lines:
        count, from_index, to_index = re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
        count = int(count)
        from_index = int(from_index) - 1
        to_index = int(to_index) - 1
        for i in range(count):
            crate = stacks[from_index].pop()
            stacks[to_index].append(crate)
    crate_tops = [stack[-1] for stack in stacks]
    print("Answer 1:", "".join(crate_tops))

    stacks = stacks_copy
    for line in lines:
        count, from_index, to_index = re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
        count = int(count)
        from_index = int(from_index) - 1
        to_index = int(to_index) - 1
        crates = stacks[from_index][-count:]
        stacks[from_index] = stacks[from_index][:-count]
        stacks[to_index].extend(crates)
    crate_tops = [stack[-1] for stack in stacks]
    print("Answer 2:", "".join(crate_tops))
