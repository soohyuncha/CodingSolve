def map_update(map_2d, direction):
    map_2d_updated = []
    for i in range(N):
        map_2d_updated.append([])
        for j in range(N):
            map_2d_updated[i].append(0)

    if direction == "up":
        # Move all non-zero values upward
        for j in range(N):
            non_zero_row_idx = 0
            for i in range(N):
                if map_2d[i][j] > 0:
                    map_2d_updated[non_zero_row_idx][j] = map_2d[i][j]
                    non_zero_row_idx += 1
        for i in range(N - 1):
            for j in range(N):
                # Merge (i, j) and (i + 1, j) => (i, j)
                if map_2d_updated[i][j] > 0 and map_2d_updated[i][j] == map_2d_updated[i + 1][j]:
                    map_2d_updated[i][j] = 2 * map_2d_updated[i][j]
                    # Move all blocks below (i, j) upward
                    for ii in range(i + 1, N):
                        if ii < N - 1:
                            map_2d_updated[ii][j] = map_2d_updated[ii + 1][j]
                            map_2d_updated[ii + 1][j] = 0
                        else:
                            map_2d_updated[ii][j] = 0
                
    elif direction == "left":
        # Move all non-zero values leftward
        for i in range(N):
            non_zero_col_idx = 0
            for j in range(N):
                if map_2d[i][j] > 0:
                    map_2d_updated[i][non_zero_col_idx] = map_2d[i][j]
                    non_zero_col_idx += 1
        for i in range(N):
            for j in range(N - 1):
                # Merge (i, j) and (i, j + 1) => (i, j)
                if map_2d_updated[i][j] > 0 and map_2d_updated[i][j] == map_2d_updated[i][j + 1]:
                    map_2d_updated[i][j] = 2 * map_2d_updated[i][j]
                    # Move all blocks right to (i, j) leftward
                    for jj in range(j + 1, N):
                        if jj < N - 1:
                            map_2d_updated[i][jj] = map_2d_updated[i][jj + 1]
                            map_2d_updated[i][jj + 1] = 0
                        else:
                            map_2d_updated[i][jj] = 0
                elif map_2d_updated[i][j] == 0:
                    for jj in range(j, N - 1):
                        map_2d_updated[i][jj] = map_2d_updated[i][jj + 1]
                    map_2d_updated[i][N - 1] = 0
    elif direction == "down":
        # Move all non-zero values downward
        for j in range(N):
            non_zero_row_idx = N - 1
            for i in range(N - 1, -1, -1):
                if map_2d[i][j] > 0:
                    map_2d_updated[non_zero_row_idx][j] = map_2d[i][j]
                    non_zero_row_idx -= 1
        for i in range(N - 1, 0, -1):
            for j in range(N):
                # Merge (i, j) and (i - 1, j) => (i, j)
                if map_2d_updated[i][j] > 0 and map_2d_updated[i][j] == map_2d_updated[i - 1][j]:
                    map_2d_updated[i][j] = 2 * map_2d_updated[i][j]
                    # Move all blocks above (i, j) downward
                    for ii in range(i - 1, -1, -1):
                        if ii > 0:
                            map_2d_updated[ii][j] = map_2d_updated[ii - 1][j]
                            map_2d_updated[ii - 1][j] = 0
                        else:
                            map_2d_updated[ii][j] = 0
                elif map_2d_updated[i][j] == 0:
                    for ii in range(i, 0, -1):
                        map_2d_updated[ii][j] = map_2d_updated[ii - 1][j]
                    map_2d_updated[0][j] = 0
    elif direction == "right":
        # Move all non-zero values rightward
        for i in range(N):
            non_zero_col_idx = N - 1
            for j in range(N - 1, -1, -1):
                if map_2d[i][j] > 0:
                    map_2d_updated[i][non_zero_col_idx] = map_2d[i][j]
                    non_zero_col_idx -= 1
        for i in range(N):
            for j in range(N - 1, 0, -1):
                # Merge (i, j) and (i, j - 1) => (i, j)
                if map_2d_updated[i][j] > 0 and map_2d_updated[i][j] == map_2d_updated[i][j - 1]:
                    map_2d_updated[i][j] = 2 * map_2d_updated[i][j]
                    # Move all blocks left to (i, j) rightward
                    for jj in range(j - 1, -1, -1):
                        if jj > 0:
                            map_2d_updated[i][jj] = map_2d_updated[i][jj - 1]
                            map_2d_updated[i][jj - 1] = 0
                        else:
                            map_2d_updated[i][jj] = 0
                elif map_2d_updated[i][j] == 0:
                    for jj in range(j, 0, -1):
                        map_2d_updated[i][jj] = map_2d_updated[i][jj - 1]
                    map_2d_updated[i][0] = 0
    return map_2d_updated

def find_max(map_2d, iter_cnt, N):
    # Find max values among the current 2D map
    cur_max = 0
    for i in range(N):
        for j in range(N):
            cur_max = max(cur_max, map_2d[i][j])
    
    # Maximum search depth = 5
    if iter_cnt == 5:
        return cur_max
    
    # DFS for all four directions
    for direction in ["up", "left", "down", "right"]:
        map_2d_updated = map_update(map_2d, direction)
        direction_max = find_max(map_2d_updated, iter_cnt + 1, N)
        cur_max = max(cur_max, direction_max)
    return cur_max

if __name__ == '__main__':
    N = int(input())
    map_2d = []
    for i in range(N):
        row = input().strip().split(' ')
        for i in range(N):
            row[i] = int(row[i])
        map_2d.append(row)
    
    result = find_max(map_2d, 0, N)
    print(result)
    