import itertools

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').readlines()
    nums = [int(line.strip()) if line.strip() else None for line in lines]
    elves = [list(group) for is_none, group in itertools.groupby(nums, lambda item: item is None) if not is_none]
    elves_calories = [sum(elf) for elf in elves]
    print('Answer one:', max(elves_calories))
    print('Answer two:', sum(sorted(elves_calories, reverse=True)[:3]))
