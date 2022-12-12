
if __name__ == '__main__':
    line = open('input.txt', encoding='utf-8').read().strip()

    unique_index = None
    for i in range(4 - 1, len(line)):
        part = line[i - 3:i + 1]
        if len(set(part)) == 4:
            unique_index = i
            break
    print("Answer 1:", unique_index + 1)

    unique_index = None
    for i in range(14 - 1, len(line)):
        part = line[i - 13:i + 1]
        if len(set(part)) == 14:
            unique_index = i
            break
    print("Answer 2:", unique_index + 1)
