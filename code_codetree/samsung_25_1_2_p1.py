def simulation(N, Q, coord_list):
    def _init_map_2d():
        map_2d = []
        for i in range(N):
            map_2d.append([])
            for j in range(N):
                map_2d[i].append(-1)
        return map_2d
    def _print_map_2d(map_2d):
        for y in range(N-1, -1, -1):
            for x in range(N):
                print(f'{map_2d[y][x]}', end=' ')
            print()
        print()
    def _search_connected_dfs(x, y, cid, is_visited):
        if (y > N-1) or (y < 0) or (x > N-1) or (x < 0) or (map_2d[y][x] != cid) or (is_visited[y][x] > 0):
            return 0
        is_visited[y][x] = 1
        up = _search_connected_dfs(x, y+1, cid, is_visited)
        down = _search_connected_dfs(x, y-1, cid, is_visited)
        left = _search_connected_dfs(x-1, y, cid, is_visited)
        right = _search_connected_dfs(x+1, y, cid, is_visited)
        return up + down + left + right + 1

    def _is_possible_to_move_dfs(x, y, x_diff, y_diff, map_2d, map_2d_new, cid, is_visited):
        x_new, y_new = x - x_diff, y - y_diff
        is_visited[y][x] = 1
        # Can't move to here
        if (y_new > N-1) or (y_new < 0) or (x_new > N-1) or (x_new < 0) or (map_2d_new[y_new][x_new] != -1):
            return False

        if (y < N-1) and (map_2d[y+1][x] == cid) and (is_visited[y+1][x] == -1):
            up = _is_possible_to_move_dfs(x, y+1, x_diff, y_diff, map_2d, map_2d_new, cid, is_visited)
            if not up:
                return False
        if (y > 0) and (map_2d[y-1][x] == cid) and (is_visited[y-1][x] == -1):
            down = _is_possible_to_move_dfs(x, y-1, x_diff, y_diff, map_2d, map_2d_new, cid, is_visited)
            if not down:
                return False
        if (x > 0) and (map_2d[y][x-1] == cid) and (is_visited[y][x-1] == -1):
            left = _is_possible_to_move_dfs(x-1, y, x_diff, y_diff, map_2d, map_2d_new, cid, is_visited)
            if not left:
                return False
        if (x < N-1) and (map_2d[y][x+1] == cid) and (is_visited[y][x+1] == -1):
            right = _is_possible_to_move_dfs(x+1, y, x_diff, y_diff, map_2d, map_2d_new, cid, is_visited)
            if not right:
                return False
        return True

    map_2d = _init_map_2d()
    old_cid_dict = {}       # ([cid]: {num_objects})
    for cid in range(Q):
        x1, y1, x2, y2 = coord_list.pop(0)
        # Step 1-1. Feed new class
        for y in range(y1, y2):
            for x in range(x1, x2):
                if map_2d[y][x] >= 0:
                    old_cid_dict[map_2d[y][x]] -= 1
                map_2d[y][x] = cid
        removed_cid = []
        for old_cid in old_cid_dict.keys():
            if old_cid_dict[old_cid] == 0:
                removed_cid.append(old_cid)
        for old_cid in removed_cid:
            old_cid_dict.pop(old_cid)
        # Step 1-2. Check existing classes
        removed_cid = []
        for old_cid in old_cid_dict.keys():
            old_cid_num_objects = old_cid_dict[old_cid]
            starting_point = None
            for y in range(N):
                for x in range(N):
                    if map_2d[y][x] == old_cid:
                        starting_point = (x, y)
                        break
                if starting_point is not None:
                    break
            
            is_visited = _init_map_2d()
            num_objects_connected = _search_connected_dfs(starting_point[0], starting_point[1], old_cid, is_visited)
            # Init class if not fully connected
            if num_objects_connected != old_cid_num_objects:
                for y in range(N):
                    for x in range(N):
                        if map_2d[y][x] == old_cid:
                            map_2d[y][x] = -1
                removed_cid.append(old_cid)
        for old_cid in removed_cid:
            old_cid_dict.pop(old_cid)
        
        # Append new class id
        old_cid_dict[cid] = (y2-y1)*(x2-x1)
        #print(old_cid_dict)
        #_print_map_2d(map_2d)

        # Step 2. Move
        map_2d_new = _init_map_2d()
        # Sort in order of "size"
        sorted_old_cid_list = sorted(old_cid_dict.items(), key=lambda x: (-x[1], x[0]))
        for cid_item in sorted_old_cid_list:
            old_cid = cid_item[0]
            # Find starting point
            starting_point = None
            for y in range(N):
                for x in range(N):
                    if map_2d[y][x] == old_cid:
                        starting_point = (x, y)
                        break
                if starting_point is not None:
                    break
            # Determine whether each new starting point is possible
            is_possible = False
            # x is priority
            for x in range(N):
                for y in range(N):
                    x_diff, y_diff = starting_point[0] - x, starting_point[1] - y
                    is_visited = _init_map_2d()
                    if _is_possible_to_move_dfs(starting_point[0], starting_point[1], x_diff, y_diff, map_2d, map_2d_new, old_cid, is_visited):
                        is_possible = True
                        new_x_diff, new_y_diff = x_diff, y_diff
                        break
                if is_possible:
                    break
            #print(starting_point, new_x_diff, new_y_diff)
            # Move to new 2D map
            if is_possible:
                for y in range(N):
                    for x in range(N):
                        if map_2d[y][x] == old_cid:
                            new_x, new_y = x - new_x_diff, y - new_y_diff
                            map_2d_new[new_y][new_x] = old_cid
            else:
                old_cid_dict.pop(old_cid)
        #_print_map_2d(map_2d_new)

        for y in range(N):
            for x in range(N):
                map_2d[y][x] = map_2d_new[y][x]

        # Step 3. Print
        result = 0
        for old_cid in old_cid_dict.keys():
            adjacent = []
            for y in range(N):
                for x in range(N):
                    if (map_2d[y][x] == old_cid):
                        # Up
                        if (y < N-1) and (map_2d[y+1][x] > old_cid) and not (map_2d[y+1][x] in adjacent):
                            adjacent.append(map_2d[y+1][x])
                        # Down
                        if (y > 0) and (map_2d[y-1][x] > old_cid) and not (map_2d[y-1][x] in adjacent):
                            adjacent.append(map_2d[y-1][x])
                        # Left
                        if (x > 0) and (map_2d[y][x-1] > old_cid) and not (map_2d[y][x-1] in adjacent):
                            adjacent.append(map_2d[y][x-1])
                        # Right
                        if (x < N-1) and (map_2d[y][x+1] > old_cid) and not (map_2d[y][x+1] in adjacent):
                            adjacent.append(map_2d[y][x+1])
            for adj_cid in adjacent:
                result += old_cid_dict[old_cid] * old_cid_dict[adj_cid]
        print(result)

if __name__ == '__main__':
    """
8 4
2 2 5 6
2 3 5 8
2 0 5 3
1 1 6 6
    """
    line = input().strip().split(' ')
    N, Q = int(line[0]), int(line[1])
    coord_list = []
    for i in range(Q):
        line = input().strip().split(' ')
        r1, c1, r2, c2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        coord_list.append((r1, c1, r2, c2))
    simulation(N, Q, coord_list)