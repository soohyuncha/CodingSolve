import sys
sys.setrecursionlimit(10**6)

def print_2d(map_2d):
    for i in range(len(map_2d)):
        for j in range(len(map_2d)):
            print(map_2d[i][j], end=' ')
        print()
    print()

def _get_rotated_dir(cur_dir, left_or_right):
    # 'L': rotate left
    # 'D': rotate right
    if left_or_right == 'L':
        if cur_dir == 'up':
            next_dir = 'left'
        elif cur_dir == 'left':
            next_dir = 'down'
        elif cur_dir == 'down':
            next_dir = 'right'
        elif cur_dir == 'right':
            next_dir = 'up'
    elif left_or_right == 'D':
        if cur_dir == 'up':
            next_dir = 'right'
        elif cur_dir == 'left':
            next_dir = 'up'
        elif cur_dir == 'down':
            next_dir = 'left'
        elif cur_dir == 'right':
            next_dir = 'down'
    return next_dir

def run_game(map_2d, dir_change, cur_head, cur_dir, second, head_history):
    # Move head
    cur_head_row, cur_head_col = cur_head
    if cur_dir == 'up':
        cur_head_row -= 1
    elif cur_dir == 'left':
        cur_head_col -= 1
    elif cur_dir == 'down':
        cur_head_row += 1
    elif cur_dir == 'right':
        cur_head_col += 1
    
    # Check terminated condition;
    # 1) Out of the map
    # 2) Match the snake position
    if cur_head_row >= len(map_2d) or cur_head_row < 0 or cur_head_col >= len(map_2d) or cur_head_col < 0 or map_2d[cur_head_row][cur_head_col] == 'o':
        return second + 1

    # Check whether apple is in the new position
    if map_2d[cur_head_row][cur_head_col] != 'x':
        tail_row, tail_col = head_history.pop(0)
        map_2d[tail_row][tail_col] = '.'

    map_2d[cur_head_row][cur_head_col] = 'o'
    head_history.append((cur_head_row, cur_head_col))

    # Determine next direction
    second += 1
    if len(dir_change) > 0 and dir_change[0][0] == second :
        next_dir_info = dir_change.pop(0)
        next_dir = _get_rotated_dir(cur_dir=cur_dir, left_or_right=next_dir_info[1])
    else:
        next_dir = cur_dir

    return run_game(map_2d, dir_change, (cur_head_row, cur_head_col), next_dir, second, head_history)
    

if __name__ == '__main__':
    ################
    # Map symbol
    # . => empty
    # x => apple
    # o => snake
    ################
    N = int(input())
    map_2d = []
    for i in range(N):
        map_2d.append([])
        for j in range(N):
            map_2d[i].append('.')

    K = int(input())
    for i in range(K):
        row = input().strip().split(' ')
        r, c = int(row[0]) - 1, int(row[1]) - 1
        map_2d[r][c] = 'x'
    map_2d[0][0] = 'o'

    L = int(input())
    dir_change = []
    for i in range(L):
        row = input().strip().split(' ')
        dir_change.append((int(row[0]), row[1]))

    result = run_game(map_2d, dir_change, cur_head=(0, 0), cur_dir='right', second=0, head_history=[(0, 0)])
    print(result)
    