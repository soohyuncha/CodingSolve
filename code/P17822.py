import sys
sys.setrecursionlimit(10**6)

def print_2d(map_2d, N, M):
    for i in range(N):
        for j in range(M):
            print(map_2d[i][j], end=' ')
        print()
    print()

def _rotate(map_2d, N, M, xi, di, ki):
    for i in range(N):
        # Check disk id is multiple of "xi"
        if (i + 1) % xi != 0:
            continue
        # Temporary list for storing rotated result of i-th disk
        tmp_i = [0 for j in range(M)]
        # Case 1. Clockwise
        if di == 0 :
            for j in range(M):
                tmp_i[(j + ki) % M] = map_2d[i][j]
        # Case 2. Counterclockwise
        elif di == 1 :
            for j in range(M):
                tmp_i[(j - ki) % M] = map_2d[i][j]
        # Copy result into "map_2d"
        for j in range(M):
            map_2d[i][j] = tmp_i[j]
    
def rotate_disk(map_2d, commands, N, M):
    #############################
    # Termination
    #############################
    if len(commands) == 0:
        num_sum = 0
        for i in range(N):
            for j in range(M):
                if map_2d[i][j] != 'x':
                    num_sum += map_2d[i][j]
        return num_sum
    # If none of elements are valid, then return immediately
    is_map_valid = False
    for i in range(N):
        for j in range(M):
            if map_2d[i][j] != 'x':
                is_map_valid = True
                break
        if is_map_valid:
            break
    if not is_map_valid:
        return 0
    
    #############################
    # Processing command
    #############################
    xi, di, ki = commands.pop(0)
    # 1) Rotate
    _rotate(map_2d, N, M, xi, di, ki)

    # 2) Check adjacency
    # True: at least one adjacent element is the same
    # False: no adjacent elements are the same
    # adjacency for all (i, j) is False, then "flag" becomes False
    adjacency = [[False for j in range(M)] for i in range(N)]
    adjacency_flag = False
    for i in range(N):
        for j in range(M):
            if map_2d[i][j] != 'x' and map_2d[i][j] == map_2d[i][(j + 1) % M]:
                adjacency[i][j] = True
            elif map_2d[i][j] != 'x' and map_2d[i][j] == map_2d[i][(j - 1) % M]:
                adjacency[i][j] = True
            elif map_2d[i][j] != 'x' and i > 0 and map_2d[i][j] == map_2d[i - 1][j]:
                adjacency[i][j] = True
            elif map_2d[i][j] != 'x' and i < N - 1 and map_2d[i][j] == map_2d[i + 1][j]:
                adjacency[i][j] = True
            
            if adjacency[i][j]:
                adjacency_flag = True
    # 3) Update map
    # 3-1) Case 1. Remove all adjacent and same elements
    if adjacency_flag:
        for i in range(N):
            for j in range(M):
                if adjacency[i][j]:
                    map_2d[i][j] = 'x'
    else:
        avg = 0
        num_nonzero_elem = 0
        for i in range(N):
            for j in range(M):
                if map_2d[i][j] != 'x':
                    num_nonzero_elem += 1
                    avg += map_2d[i][j]
        avg = avg / num_nonzero_elem
        for i in range(N):
            for j in range(M):
                if map_2d[i][j] != 'x':
                    if map_2d[i][j] > avg:
                        map_2d[i][j] -= 1
                    elif map_2d[i][j] < avg:
                        map_2d[i][j] += 1
    
    # 4) Move to next command
    return rotate_disk(map_2d, commands, N, M)

if __name__ == '__main__':
    row = input().strip().split(' ')
    N, M, T = int(row[0]), int(row[1]), int(row[2])

    map_2d = []
    for i in range(N):
        row = input().strip().split(' ')
        map_2d.append(row)
        for j in range(M):
            map_2d[i][j] = int(map_2d[i][j])
    
    commands = []
    for i in range(T):
        row = input().strip().split(' ')
        commands.append(row)
        for j in range(3):
            commands[i][j] = int(commands[i][j])
    
    result = rotate_disk(map_2d, commands, N, M)
    print(result)