import sys
sys.setrecursionlimit(10**6)

def print_2d(map_2d):
    for i in range(len(map_2d)):
        for j in range(len(map_2d[0])):
            print(map_2d[i][j], end=' ')
        print()
    print()

def _roll_dice(command, dice_pos, dice, N, M):
    dice_row, dice_col = dice_pos
    up, down, north, west, south, east = dice
    # roll to east
    if command == 1 and dice_col < M - 1:
        dice_col += 1
        up, down, north, west, south, east = west, east, north, down, south, up
    # roll to west
    elif command == 2 and dice_col > 0:
        dice_col -= 1
        up, down, north, west, south, east = east, west, north, up, south, down
    # roll to north
    elif command == 3 and dice_row > 0:
        dice_row -= 1
        up, down, north, west, south, east = south, north, up, west, down, east
    # roll to south
    elif command == 4 and dice_row < N - 1:
        dice_row += 1
        up, down, north, west, south, east = north, south, down, west, up, east
    
    return (dice_row, dice_col), (up, down, north, west, south, east)

def run_command(map_2d, commands, dice_pos, dice, N, M):
    if len(commands) == 0:
        return
    # dice_pos: [row, col]
    # dice: [up, down, north, west, south, east]
    com = commands.pop(0)
    new_dice_pos, new_dice = _roll_dice(com, dice_pos, dice, N, M)
    new_dice_row, new_dice_col = new_dice_pos
    up, down, north, west, south, east = new_dice

    # We cannot move dice
    if (dice_pos[0] == new_dice_pos[0]) and (dice_pos[1] == new_dice_pos[1]) :
        pass
    else:
        if map_2d[new_dice_row][new_dice_col] == 0:
            map_2d[new_dice_row][new_dice_col] = down
        else:
            down = map_2d[new_dice_row][new_dice_col]
            map_2d[new_dice_row][new_dice_col] = 0
        result = up
        print(result)
    return run_command(map_2d, commands, new_dice_pos, dice=(up, down, north, west, south, east), N=N, M=M)


if __name__ == '__main__':
    command = input().strip().split(' ')
    N, M, x, y, K = int(command[0]), int(command[1]), int(command[2]), int(command[3]), int(command[4])
    map_2d = []
    for i in range(N):
        map_2d.append(input().strip().split(' '))
        for j in range(M):
            map_2d[i][j] = int(map_2d[i][j])
    commands = input().strip().split(' ')
    for i in range(K):
        commands[i] = int(commands[i])
    
    run_command(map_2d, commands, dice_pos=(x, y), dice=(0, 0, 0, 0, 0, 0), N=N, M=M)