def map_update(direction, red_pos, blue_pos, hole_pos, iter_cnt, map_2d, N, M):
    red_row, red_col, blue_row, blue_col = red_pos[0], red_pos[1], blue_pos[0], blue_pos[1]
    red_hole, blue_hole, pos_update = False, False, True
    if direction == "up":
        while pos_update:
            pos_update = False
            if (hole_pos[0] == red_row) and (hole_pos[1] == red_col):
                red_hole = True
                red_row, red_col = -1, -1       # Invalidate red pos
            if (hole_pos[0] == blue_row) and (hole_pos[1] == blue_col):
                blue_hole = True
                blue_row, blue_col = -1, -1       # Invalidate blue pos

            # Two are in the same column, and red is upper; Process red one first
            if (red_col == blue_col) and (red_row < blue_row):
                if (not red_hole) and (red_row > 0) and (map_2d[red_row - 1][red_col] != "#"):
                    red_row -= 1
                    pos_update = True
                if (not blue_hole) and (blue_row > 0) and (map_2d[blue_row - 1][blue_col] != "#") and (blue_row - 1 != red_row):
                    blue_row -= 1
                    pos_update = True
            # Two are in the same column, and blue is upper; Process blue one first
            elif (red_col == blue_col) and (red_row > blue_row):
                if (not blue_hole) and (blue_row > 0) and (map_2d[blue_row - 1][blue_col] != "#"):
                    blue_row -= 1
                    pos_update = True
                if (not red_hole) and (red_row > 0) and (map_2d[red_row - 1][red_col] != "#") and (red_row - 1 != blue_row):
                    red_row -= 1
                    pos_update = True
            # Two are in the different columns; Processing order doesn't matter
            else:
                if (not red_hole) and (red_row > 0) and (map_2d[red_row - 1][red_col] != "#"):
                    red_row -= 1
                    pos_update = True
                if (not blue_hole) and (blue_row > 0) and (map_2d[blue_row - 1][blue_col] != "#"):
                    blue_row -= 1
                    pos_update = True
    
    elif direction == "left":
        while pos_update:
            pos_update = False
            if (hole_pos[0] == red_row) and (hole_pos[1] == red_col):
                red_hole = True
                red_row, red_col = -1, -1       # Invalidate red pos
            if (hole_pos[0] == blue_row) and (hole_pos[1] == blue_col):
                blue_hole = True
                blue_row, blue_col = -1, -1       # Invalidate blue pos

            # Two are in the same column, and red is left; Process red one first
            if (red_row == blue_row) and (red_col < blue_col):
                if (not red_hole) and (red_col > 0) and (map_2d[red_row][red_col - 1] != "#"):
                    red_col -= 1
                    pos_update = True
                if (not blue_hole) and (blue_col > 0) and (map_2d[blue_row][blue_col - 1] != "#") and (blue_col - 1 != red_col):
                    blue_col -= 1
                    pos_update = True
            # Two are in the same row, and blue is left; Process blue one first
            elif (red_row == blue_row) and (red_col > blue_col):
                if (not blue_hole) and (blue_col > 0) and (map_2d[blue_row][blue_col - 1] != "#"):
                    blue_col -= 1
                    pos_update = True
                if (not red_hole) and (red_col > 0) and (map_2d[red_row][red_col - 1] != "#") and (red_col - 1 != blue_col):
                    red_col -= 1
                    pos_update = True
            # Two are in the different rows; Processing order doesn't matter
            else:
                if (not red_hole) and (red_col > 0) and (map_2d[red_row][red_col - 1] != "#"):
                    red_col -= 1
                    pos_update = True
                if (not blue_hole) and (blue_col > 0) and (map_2d[blue_row][blue_col - 1] != "#"):
                    blue_col -= 1
                    pos_update = True

    elif direction == "down":
        while pos_update:
            pos_update = False
            if (hole_pos[0] == red_row) and (hole_pos[1] == red_col):
                red_hole = True
                red_row, red_col = -1, -1       # Invalidate red pos
            if (hole_pos[0] == blue_row) and (hole_pos[1] == blue_col):
                blue_hole = True
                blue_row, blue_col = -1, -1       # Invalidate blue pos

            # Two are in the same column, and red is lower; Process red one first
            if (red_col == blue_col) and (red_row > blue_row):
                if (not red_hole) and (red_row < N - 1) and (map_2d[red_row + 1][red_col] != "#"):
                    red_row += 1
                    pos_update = True
                if (not blue_hole) and (blue_row < N - 1) and (map_2d[blue_row + 1][blue_col] != "#") and (blue_row + 1 != red_row):
                    blue_row += 1
                    pos_update = True
            # Two are in the same column, and blue is lower; Process blue one first
            elif (red_col == blue_col) and (red_row < blue_row):
                if (not blue_hole) and (blue_row < N - 1) and (map_2d[blue_row + 1][blue_col] != "#"):
                    blue_row += 1
                    pos_update = True
                if (not red_hole) and (red_row < N - 1) and (map_2d[red_row + 1][red_col] != "#") and (red_row + 1 != blue_row):
                    red_row += 1
                    pos_update = True
            # Two are in the different columns; Processing order doesn't matter
            else:
                if (not red_hole) and (red_row < N - 1) and (map_2d[red_row + 1][red_col] != "#"):
                    red_row += 1
                    pos_update = True
                if (not blue_hole) and (blue_row < N - 1) and (map_2d[blue_row + 1][blue_col] != "#"):
                    blue_row += 1
                    pos_update = True

    elif direction == "right":
        while pos_update:
            pos_update = False
            if (hole_pos[0] == red_row) and (hole_pos[1] == red_col):
                red_hole = True
                red_row, red_col = -1, -1       # Invalidate red pos
            if (hole_pos[0] == blue_row) and (hole_pos[1] == blue_col):
                blue_hole = True
                blue_row, blue_col = -1, -1       # Invalidate blue pos

            # Two are in the same row, and red is right; Process red one first
            if (red_row == blue_row) and (red_col > blue_col):
                if (not red_hole) and (red_col > 0) and (map_2d[red_row][red_col + 1] != "#"):
                    red_col += 1
                    pos_update = True
                if (not blue_hole) and (blue_col > 0) and (map_2d[blue_row][blue_col + 1] != "#") and (blue_col + 1 != red_col):
                    blue_col += 1
                    pos_update = True
            # Two are in the same row, and blue is right; Process blue one first
            elif (red_row == blue_row) and (red_col < blue_col):
                if (not blue_hole) and (blue_col > 0) and (map_2d[blue_row][blue_col + 1] != "#"):
                    blue_col += 1
                    pos_update = True
                if (not red_hole) and (red_col > 0) and (map_2d[red_row][red_col + 1] != "#") and (red_col + 1 != blue_col):
                    red_col += 1
                    pos_update = True
            # Two are in the different rows; Processing order doesn't matter
            else:
                if (not red_hole) and (red_col > 0) and (map_2d[red_row][red_col + 1] != "#"):
                    red_col += 1
                    pos_update = True
                if (not blue_hole) and (blue_col > 0) and (map_2d[blue_row][blue_col + 1] != "#"):
                    blue_col += 1
                    pos_update = True

    if red_hole and (not blue_hole):
        result = 0
    elif blue_hole:
        result = 1
    elif red_row == red_pos[0] and red_col == red_pos[1] and blue_row == blue_pos[0] and blue_col == blue_pos[1]:
        result = 1
    else:
        result = 2
    return (red_row, red_col), (blue_row, blue_col), result

def find_goal(direction, red_pos, blue_pos, hole_pos, iter_cnt, map_2d, N, M):
    if iter_cnt > 10:
        return None
    if direction is not None:
        red_pos, blue_pos, result = map_update(direction, red_pos, blue_pos, hole_pos, iter_cnt, map_2d, N, M)
        # Case 1. Red get in the hole
        if result == 0:
            return iter_cnt
        # Case 2. Blue get in the hole; None of the pos are updated
        elif result == 1:
            return None
        # Case 3. None get in the hole; Continue the search
        else:
            pass
    
    result_final = -1
    for next_direction in ["up", "left", "down", "right"]:
        result = find_goal(next_direction, red_pos, blue_pos, hole_pos, iter_cnt + 1, map_2d, N, M)
        
        if result is not None and result > 0:
            result_final = min(result_final, result) if result_final > 0 else result
    
    return result_final


if __name__ == '__main__':
    board_spec = input().strip().split(' ')
    N, M = int(board_spec[0]), int(board_spec[1])
    map_2d = []
    for i in range(N):
        map_row_str = input()
        map_row = []
        for j in range(M):
            map_row.append(map_row_str[j])
        map_2d.append(map_row)

    for i in range(N):
        for j in range(M):
            if map_2d[i][j] == 'R':
                map_2d[i][j] = '.'      # replace with dot
                red_pos = (i, j)
            elif map_2d[i][j] == 'B':
                map_2d[i][j] = '.'      # replace with dot
                blue_pos = (i, j)
            elif map_2d[i][j] == 'O':
                hole_pos = (i, j)


    ans = find_goal(None, red_pos, blue_pos, hole_pos, 0, map_2d, N, M)
    print(ans)