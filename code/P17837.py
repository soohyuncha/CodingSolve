import sys
sys.setrecursionlimit(10**6)

def print_2d(map_2d):
    print('====================')
    for i in range(len(map_2d)):
        for j in range(len(map_2d)):
            if len(map_2d[i][j].object_list) > 0:
                print(f'({i}, {j})')
                for k in range(len(map_2d[i][j].object_list)):
                    print(map_2d[i][j].object_list[k].obj_id, end=' -> ')
                print()
    print('====================')
    print()

class Point:
    def __init__(self, color, object_list):
        self.color = color
        self.object_list = object_list

class Object:
    def __init__(self, obj_id, direction):
        self.obj_id = obj_id
        self.direction = direction

def _get_next_pos(r, c, direction):
    if direction == 1:
        return (r, c + 1)
    elif direction == 2:
        return (r, c - 1)
    elif direction == 3:
        return (r - 1, c)
    elif direction == 4:
        return (r + 1, c)
    
def _get_opposite_dir(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3
    
def play_turn(map_2d, object_position, turn, N):
    if turn == 1000:
        return -1
    turn += 1

    for i in range(len(object_position)):
        r, c = object_position[i]
        pos_obj_len = len(map_2d[r][c].object_list)
        for j in range(len(map_2d[r][c].object_list)):
            if map_2d[r][c].object_list[j].obj_id == i:
                obj = map_2d[r][c].object_list[j]
                obj_idx_in_pos = j
                break
        r_next, c_next = _get_next_pos(r, c, obj.direction)
        # Case 1. Next position is "white"
        if r_next >= 0 and r_next < N and c_next >= 0 and c_next < N and map_2d[r_next][c_next].color == 0:
            for j in range(pos_obj_len - obj_idx_in_pos):
                obj = map_2d[r][c].object_list.pop(obj_idx_in_pos)
                map_2d[r_next][c_next].object_list.append(obj)
                object_position[obj.obj_id] = (r_next, c_next)
            if len(map_2d[r_next][c_next].object_list) >= 4:
                return turn
            #print(f'Move {obj.obj_id} from ({r}, {c}) -> ({r_next}, {c_next})')
        # Case 2. Next position is "red"
        elif r_next >= 0 and r_next < N and c_next >= 0 and c_next < N and map_2d[r_next][c_next].color == 1:
            for j in range(pos_obj_len - obj_idx_in_pos):
                obj = map_2d[r][c].object_list.pop(-1)
                map_2d[r_next][c_next].object_list.append(obj)
                object_position[obj.obj_id] = (r_next, c_next)
            if len(map_2d[r_next][c_next].object_list) >= 4:
                return turn
            #print(f'Move {obj.obj_id} from ({r}, {c}) -> ({r_next}, {c_next})')
        # Case 3. Next position is "blue" or "out of the map"
        else:
            direction = _get_opposite_dir(obj.direction)
            obj.direction = direction
            r_next, c_next = _get_next_pos(r, c, obj.direction)
            if r_next >= 0 and r_next < N and c_next >= 0 and c_next < N and map_2d[r_next][c_next].color == 0:
                for j in range(pos_obj_len - obj_idx_in_pos):
                    obj = map_2d[r][c].object_list.pop(obj_idx_in_pos)
                    map_2d[r_next][c_next].object_list.append(obj)
                    object_position[obj.obj_id] = (r_next, c_next)
                if len(map_2d[r_next][c_next].object_list) >= 4:
                    return turn
                #print(f'Move {obj.obj_id} from ({r}, {c}) -> ({r_next}, {c_next})')
            elif r_next >= 0 and r_next < N and c_next >= 0 and c_next < N and map_2d[r_next][c_next].color == 1:
                for j in range(pos_obj_len - obj_idx_in_pos):
                    obj = map_2d[r][c].object_list.pop(-1)
                    map_2d[r_next][c_next].object_list.append(obj)
                    object_position[obj.obj_id] = (r_next, c_next)
                if len(map_2d[r_next][c_next].object_list) >= 4:
                    return turn
            #print(f'Move {obj.obj_id} from ({r}, {c}) -> ({r_next}, {c_next})')
    #print_2d(map_2d)
    
    #exit()
    # Check termination condition
    for r in range(N):
        for c in range(N):
            if len(map_2d[r][c].object_list) >= 4:
                return turn
    return play_turn(map_2d, object_position, turn, N)

if __name__ == '__main__':
    row = input().strip().split(' ')
    N, K = int(row[0]), int(row[1])
    map_2d = []
    # 0: White, 1: Red, 2: Blue
    for i in range(N):
        map_2d.append([])
        row = input().strip().split(' ')
        for j in range(N):
            map_2d[i].append(Point(color=int(row[j]), object_list=[]))

    object_position = []
    # 1: Right, 2: Left, 3: Up, 4: Down
    for i in range(K):
        row = input().strip().split(' ')
        r, c, direction = int(row[0]) - 1, int(row[1]) - 1, int(row[2])
        map_2d[r][c].object_list.append(Object(obj_id=i, direction=direction))
        object_position.append((r, c))
    #print_2d(map_2d)
    result = play_turn(map_2d, object_position, turn=0, N=N)
    print(result)