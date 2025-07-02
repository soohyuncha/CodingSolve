class Shark:
    def __init__(self, speed, direction, size, is_updated):
        self.speed = speed
        self.direction = direction
        self.size = size
        self.is_updated = is_updated

def _move_shark(R, C, r, c, speed, direction):
    remaining_distance = speed
    # Loop until remaining distance > 0
    while 1:
        # Case 1. Upward
        if direction == 1:
            maximum_distance = min(r, remaining_distance)
            r -= maximum_distance
            remaining_distance -= maximum_distance
            if remaining_distance > 0:
                direction = 2
            else:
                break
        # Case 2. Downward
        elif direction == 2:
            maximum_distance = min(R - 1 - r, remaining_distance)
            r += maximum_distance
            remaining_distance -= maximum_distance
            if remaining_distance > 0:
                direction = 1
            else:
                break
        # Case 3. Rightward
        elif direction == 3:
            maximum_distance = min(C - 1 - c, remaining_distance)
            c += maximum_distance
            remaining_distance -= maximum_distance
            if remaining_distance > 0:
                direction = 4
            else:
                break
        # Case 4. Leftward
        elif direction == 4:
            maximum_distance = min(c, remaining_distance)
            c -= maximum_distance
            remaining_distance -= maximum_distance
            if remaining_distance > 0:
                direction = 3
            else:
                break
    return (r, c), direction

def simulate_fishing(map_2d, R, C, man_pos, num_sharks):
    man_pos += 1
    if man_pos == C:
        return num_sharks
    # 1) Get shark if possible
    for i in range(R):
        if len(map_2d[i][man_pos]) > 0:
            num_sharks += map_2d[i][man_pos][0].size
            map_2d[i][man_pos] = []      # Remove shark from the position
            break
    
    # 2) Move each shark
    for r in range(R):
        for c in range(C):
            # The position has at least one shark that is not updated yet
            while (len(map_2d[r][c]) > 0) and (not map_2d[r][c][0].is_updated):
                shark = map_2d[r][c].pop(0)
                new_pos, new_direction = _move_shark(R, C, r, c, shark.speed, shark.direction)
                shark.is_updated = True
                shark.direction = new_direction
                map_2d[new_pos[0]][new_pos[1]].append(shark)

    # 3-1) Merge sharks if multiple sharks are in the same position
    # 3-2) Clear "is_updated" flag for next timestep
    for r in range(R):
        for c in range(C):
            if len(map_2d[r][c]) > 0:
                max_size = 0
                max_idx = -1
                for k in range(len(map_2d[r][c])):
                    shark = map_2d[r][c][k]
                    if shark.size > max_size:
                        max_size = shark.size
                        max_idx = k
                    
                map_2d[r][c] = [map_2d[r][c][max_idx]]
                map_2d[r][c][0].is_updated = False

    # Move to next timestep
    return simulate_fishing(map_2d, R, C, man_pos, num_sharks)

if __name__ == '__main__':
    row = input().strip().split(' ')
    R, C, M = int(row[0]), int(row[1]), int(row[2])
    map_2d = []
    for i in range(R):
        map_2d.append([])
        for j in range(C):
            map_2d[i].append([])

    for i in range(M):
        row = input().strip().split(' ')
        # Index start from "zero"
        r, c, s, d, z = int(row[0]) - 1, int(row[1]) - 1, int(row[2]), int(row[3]), int(row[4])
        map_2d[r][c].append(Shark(speed = s, direction = d, size = z, is_updated = False))

    result = simulate_fishing(map_2d, R, C, man_pos=-1, num_sharks=0)
    print(result)