from collections import deque
import heapq
def init_graph(map_2d, N):
    def _is_up_possible(r, c, jump):
        if (r-jump < 0) or (map_2d[r-jump][c] == "S"):
            return False
        for kk in range(1, jump+1):
            if map_2d[r-kk][c] == "#":
                return False
        return True
    def _is_down_possible(r, c, jump):
        if (r+jump > N-1) or (map_2d[r+jump][c] == "S"):
            return False
        for kk in range(1, jump+1):
            if map_2d[r+kk][c] == "#":
                return False
        return True
    def _is_left_possible(r, c, jump):
        if (c-jump < 0) or (map_2d[r][c-jump] == "S"):
            return False
        for kk in range(1, jump+1):
            if map_2d[r][c-kk] == "#":
                return False
        return True
    def _is_right_possible(r, c, jump):
        if (c+jump > N-1) or (map_2d[r][c+jump] == "S"):
            return False
        for kk in range(1, jump+1):
            if map_2d[r][c+kk] == "#":
                return False
        return True
    graph = []
    for r in range(N):
        graph.append([])
        for c in range(N):
            graph[r].append([])
            if map_2d[r][c] != ".":
                continue
            for k in range(5):
                jump = k+1
                graph[r][c].append([])
                # Case 1. Move
                if _is_up_possible(r, c, jump):
                    graph[r][c][k].append((1, r-jump, c, k))
                if _is_down_possible(r, c, jump):
                    graph[r][c][k].append((1, r+jump, c, k))
                if _is_left_possible(r, c, jump):
                    graph[r][c][k].append((1, r, c-jump, k))
                if _is_right_possible(r, c, jump):
                    graph[r][c][k].append((1, r, c+jump, k))
                # Case 2. Increase
                if jump < 5:
                    graph[r][c][k].append(((jump+1)**2, r, c, (jump+1)-1))
                # Case 3. Decrease
                if jump > 1:
                    for kk in range(1, jump):
                        graph[r][c][k].append((1, r, c, (jump-kk)-1))
    return graph

def init_visited_time(N):
    visited_time = []
    for r in range(N):
        visited_time.append([])
        for c in range(N):
            visited_time[r].append([])
            for k in range(5):
                visited_time[r][c].append(-1)
    return visited_time

def find_min(graph, visited_time, r, c, r_dst, c_dst):
    queue = []
    visited_time[r][c][0] = 0
    for item in graph[r][c][0]:
        #queue.append(item)
        heapq.heappush(queue, item)

    while queue:
        #queue.sort(key=lambda x: x[0])
        #time, r, c, k = queue.pop(0)
        time, r, c, k = heapq.heappop(queue)
        visited_time[r][c][k] = time
        if (r == r_dst) and (c == c_dst):
            return time
        for item in graph[r][c][k]:
            time_to_move, r_new, c_new, k_new = item
            if (visited_time[r_new][c_new][k_new] == -1) or (time + time_to_move < visited_time[r_new][c_new][k_new]):
                visited_time[r_new][c_new][k_new] = time + time_to_move
                #queue.append((time + time_to_move, r_new, c_new, k_new))
                heapq.heappush(queue, (time + time_to_move, r_new, c_new, k_new))
    return -1
            

if __name__ == '__main__':
    """
8
.S..#.##
##.S.##.
##S#S##S
..SS.S##
.S#S.#S#
..#S...#
###....S
#.S.SS#.
5
1 1 1 3
4 1 4 5
6 2 1 1
7 4 8 8
8 2 6 1
    """
    """
8
.S..#.##
##.S.##.
##S#S##S
..SS.S##
.S#S.#S#
..#S...#
###....S
#.S.SS#.
1
6 2 1 1
    """
    N = int(input())
    map_2d = []
    for i in range(N):
        map_2d.append(list(input().strip()))
    graph = init_graph(map_2d, N)

    Q = int(input())
    input_list = []
    for i in range(Q):
        line = input().strip().split(' ')
        r1, c1, r2, c2 = int(line[0]) - 1, int(line[1]) - 1, int(line[2]) - 1, int(line[3]) - 1
        input_list.append((r1, c1, r2, c2))

    for i in range(Q):
        visited_time = init_visited_time(N)
        r1, c1, r2, c2 = input_list.pop(0)
        result = find_min(graph, visited_time, r1, c1, r2, c2)
        print(result)