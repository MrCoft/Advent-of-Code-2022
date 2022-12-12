import re

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.size} {self.name}'

class Dir:
    def __init__(self, parent, name):
        self.name = name
        self.children = []
        self.parent = parent

    def __str__(self):
        buf = []
        buf.append(f'dir {self.name}')
        for child in self.children:
            s = str(child)
            for line in s.splitlines():
                buf.append("  " + line)
        return "\n".join(buf)

    def iter_dirs(self):
        yield self
        for child in self.children:
            if isinstance(child, Dir):
                yield from child.iter_dirs()

    def iter_files(self):
        for child in self.children:
            if isinstance(child, File):
                yield child
            if isinstance(child, Dir):
                yield from child.iter_files()

    def total_size(self):
        return sum(file.size for file in self.iter_files())

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').readlines()
    line_index = 0
    def get_next_line():
        global line_index
        if line_index >= len(lines):
            return None
        line = lines[line_index]
        line_index += 1
        return line.strip()

    def put_line_back():
        global line_index
        line_index -= 1

    filesystem = Dir(None, "/")
    cwd = None

    def cd(dir):
        global cwd
        if dir == "/":
            cwd = filesystem
            return
        elif dir == '..':
            cwd = cwd.parent
        else:
            cwd = next(file for file in cwd.children if isinstance(file, Dir) and file.name == dir)

    def ls():
        while True:
            line = get_next_line()
            if line is None or line.startswith("$ "):
                put_line_back()
                return

            match = re.search(r"(\d+) (.+)", line)
            if match:
                size, name = match.groups()
                if all(file.name != name for file in cwd.children if isinstance(file, File)):
                    file = File(name, int(size))
                    cwd.children.append(file)

            match = re.search(r"dir (.+)", line)
            if match:
                (name,) = match.groups()
                if all(dir.name != name for dir in cwd.children if isinstance(dir, Dir)):
                    dir = Dir(cwd, name)
                    cwd.children.append(dir)

    while True:
        line = get_next_line()
        if line is None:
            break

        if line.startswith("$ "):
            line = line[2:]
            cmd = line.split()[0]
            args = line.split()[1:]
            eval(cmd)(*args)

    print(filesystem)

    total_size = 0
    for dir in filesystem.iter_dirs():
        if dir.total_size() <= 100000:
            total_size += dir.total_size()
    print("Answer 1:", total_size)

    max_used_space = 70000000 - 30000000
    current_used_space = filesystem.total_size()
    print("Answer 2:", min(dir.total_size() for dir in filesystem.iter_dirs() if dir.total_size() >= current_used_space - max_used_space))
