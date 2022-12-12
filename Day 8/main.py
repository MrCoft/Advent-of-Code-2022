import numpy as np
import time

DEBUG = True

if __name__ == '__main__':
    if DEBUG:
        start_time = time.perf_counter()

    lines = open('input.txt', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    width, height = len(lines[0]), len(lines)
    def get_height(pos):
        x, y = pos
        if x < 0 or y < 0 or x >= width or y >= height:
            return None
        return int(lines[y][x])

    class DirectionInfo:
        def __init__(self, pos, dir):
            self.pos = pos
            self.dir = dir
            self.depth_cache = dict()

    direction_infos = []
    for x in range(width):
        direction_infos.append(DirectionInfo(np.array([x, 0]), np.array([0, 1])))
        direction_infos.append(DirectionInfo(np.array([x, height - 1]), np.array([0, -1])))
    for y in range(height):
        direction_infos.append(DirectionInfo(np.array([0, y]), np.array([1, 0])))
        direction_infos.append(DirectionInfo(np.array([width - 1, y]), np.array([-1, 0])))

    for info in direction_infos:
        pos = info.pos
        depth = 0
        h = -1
        while True:
            height_at_pos = get_height(pos)
            if height_at_pos is None:
                for i in range(h + 1, 10):
                    info.depth_cache[i] = depth
                break
            else:
                for i in range(h + 1, height_at_pos + 1):
                    info.depth_cache[i] = depth
                if height_at_pos == 9:
                    break
            pos = pos + info.dir
            depth += 1
            h = height_at_pos if height_at_pos > h else h

    if DEBUG:
        print('Cached info for each inner direction from the edges:')
        for info in direction_infos:
            print(f'{info.pos} {str(info.dir).rjust(7)} {info.depth_cache}')
        print()

    visible_trees = 0
    if DEBUG:
        print('Comparing each position to cached directions info:')
    for x in range(width):
        for y in range(height):
            h = get_height((x, y))
            visible = False
            for info in direction_infos:
                ix, iy = info.pos
                if x == ix or y == iy:
                    depth = abs(x - ix) + abs(y - iy)
                    if DEBUG and x > 0 and y > 0 and x <= 3 and y <= 3:
                        print(f'x: {x}, y: {y}, ix: {ix}, iy: {iy}, depth: {depth}, depth_cache: {info.depth_cache[h]}')
                    if info.depth_cache[h] >= depth:
                        visible = True
            if DEBUG and x > 0 and y > 0 and x <= 3 and y <= 3:
                print(f'Visible: {visible}')
            if visible:
                visible_trees += 1
    if DEBUG:
        print()

    if DEBUG:
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"The execution time is: {execution_time}")

    print("Answer 1:", visible_trees)
    print()

    if DEBUG:
        start_time = time.perf_counter()

    class LineOfSightSegment:
        def __init__(self, start, end):
            self.start = start
            self.end = end

    lines_of_sight = [[[[] for j in range(height)] for i in range(width)] for h in range(10)]
    def insert_segment(segment, h, dir):
        # NOTE: Only insert from one side, because there will be another pass from the other direction
        insert_start = segment.start - dir
        if get_height(insert_start) is not None:
            lines_of_sight[h][insert_start[0]][insert_start[1]].append(segment)

    for info in direction_infos:
        heights = []
        pos = info.pos
        while True:
            h = get_height(pos)
            if h is None:
                break
            heights.append(h)
            pos = pos + info.dir

        for h in range(1, 10):
            segment = None
            depth = 0
            for tree_h in heights:
                if tree_h < h:
                    pos = info.pos + info.dir * depth
                    if segment is None:
                        segment = LineOfSightSegment(pos, None)
                if tree_h >= h and segment:
                    pos = info.pos + info.dir * (depth - 1)
                    segment.end = pos
                    insert_segment(segment, h, info.dir)
                    segment = None
                depth += 1
            if segment:
                segment.end = info.pos + info.dir * (len(heights) - 1)
                insert_segment(segment, h, info.dir)

    max_scenery = 0
    best_pos = None
    for x in range(width):
        for y in range(height):
            sight = lines_of_sight[get_height((x, y))][x][y]
            scenery = 1
            for s in sight:
                # NOTE: Add 1 to measure segment length
                s_len = 1 + abs(s.end[0] - s.start[0]) + abs(s.end[1] - s.start[1])
                is_num_edge = lambda x: x == 0 or x == width - 1
                is_pos_edge = lambda pos: is_num_edge(pos[0]) or is_num_edge(pos[1])
                if not (is_pos_edge(s.start) or is_pos_edge(s.end)):
                    # NOTE: If not edge, add 1 for the seen tree
                    s_len += 1
                scenery *= s_len

            if scenery > max_scenery:
                max_scenery = scenery
                best_pos = (x, y)
    if DEBUG:
        print('Best position, and its segments of lower trees:', best_pos)
        for s in lines_of_sight[get_height(best_pos)][best_pos[0]][best_pos[1]]:
            print(s.start, s.end)
        print()
    print("Answer 2:", max_scenery)

    if DEBUG:
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"The execution time is: {execution_time}")
