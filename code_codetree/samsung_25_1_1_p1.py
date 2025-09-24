def run_simulation(N, T, F, B):
    def _init_group():
        G = []
        for i in range(N):
            G.append([])
            for j in range(N):
                G[i].append(None)
        return G
    
    def _alloc_group_dfs(r, c, G, gid):
        G[r][c] = gid
        f = F[r][c]
        # Up
        if r >= 1 and G[r-1][c] is None and F[r-1][c] == f:
            _alloc_group_dfs(r-1, c, G, gid)
        # Down
        if r <= N-2 and G[r+1][c] is None and F[r+1][c] == f:
            _alloc_group_dfs(r+1, c, G, gid)
        # Left
        if c >= 1 and G[r][c-1] is None and F[r][c-1] == f:
            _alloc_group_dfs(r, c-1, G, gid)
        # Right
        if c <= N-2 and G[r][c+1] is None and F[r][c+1] == f:
            _alloc_group_dfs(r, c+1, G, gid)
    
    def _propagate_up(R, C, B, F, is_propagated, x):
        if R == 0:
            return
        r, c = R - 1, C
        while r >= 0 and x > 0:
            if F[r][c] != F[R][C]:
                # Case 1. x > y
                if x > B[r][c]:
                    x, B[r][c] = x - (B[r][c] + 1), B[r][c] + 1
                    F[r][c] = F[R][C]
                # Case 2. x <= y
                else:
                    x, B[r][c] = 0, B[r][c] + x
                    F[r][c] = F[R][C] + F[r][c]
                    F[r][c] = ''.join(set(F[r][c]))
                    F[r][c] = ''.join(sorted(list(F[r][c])))
                is_propagated[r][c] = True
            r -= 1
    
    def _propagate_down(R, C, B, F, is_propagated, x):
        if R == N-1:
            return
        r, c = R + 1, C
        while r <= N-1 and x > 0:
            if F[r][c] != F[R][C]:
                # Case 1. x > y
                if x > B[r][c]:
                    x, B[r][c] = x - (B[r][c] + 1), B[r][c] + 1
                    F[r][c] = F[R][C]
                # Case 2. x <= y
                else:
                    x, B[r][c] = 0, B[r][c] + x
                    F[r][c] = F[R][C] + F[r][c]
                    F[r][c] = ''.join(set(F[r][c]))
                    F[r][c] = ''.join(sorted(list(F[r][c])))
                is_propagated[r][c] = True
            r += 1

    def _propagate_left(R, C, B, F, is_propagated, x):
        if C == 0:
            return
        r, c = R, C - 1
        while c >= 0 and x > 0:
            if F[r][c] != F[R][C]:
                # Case 1. x > y
                if x > B[r][c]:
                    x, B[r][c] = x - (B[r][c] + 1), B[r][c] + 1
                    F[r][c] = F[R][C]
                # Case 2. x <= y
                else:
                    x, B[r][c] = 0, B[r][c] + x
                    F[r][c] = F[R][C] + F[r][c]
                    F[r][c] = ''.join(set(F[r][c]))
                    F[r][c] = ''.join(sorted(list(F[r][c])))
                is_propagated[r][c] = True
            c -= 1
    
    def _propagate_right(R, C, B, F, is_propagated, x):
        if C == N-1:
            return
        r, c = R, C + 1
        while c <= N-1 and x > 0:
            if F[r][c] != F[R][C]:
                # Case 1. x > y
                if x > B[r][c]:
                    x, B[r][c] = x - (B[r][c] + 1), B[r][c] + 1
                    F[r][c] = F[R][C]
                # Case 2. x <= y
                else:
                    x, B[r][c] = 0, B[r][c] + x
                    F[r][c] = F[R][C] + F[r][c]
                    F[r][c] = ''.join(set(F[r][c]))
                    F[r][c] = ''.join(sorted(list(F[r][c])))
                is_propagated[r][c] = True
            c += 1

    for t in range(T):
        # Step 1. Morning
        for i in range(N):
            for j in range(N):
                B[i][j] += 1
        
        # Step 2. Afternoon
        # 2-1. Assign group
        G = _init_group()
        gid = 0
        for i in range(N):
            for j in range(N):
                if G[i][j] is None:
                    _alloc_group_dfs(i, j, G, gid)
                    gid += 1
        # 2-2. Find group max
        G_dict = {}
        for i in range(N):
            for j in range(N):
                gid = G[i][j]
                if not (gid in G_dict):
                    G_dict[gid] = []
                G_dict[gid].append((B[i][j], i, j))
        G_max_dict = {}
        for gid in G_dict.keys():
            group = G_dict[gid]
            group.sort(key=lambda x: (-x[0], x[1], x[2]))
            G_max_dict[gid] = (group[0][1], group[0][2])        # Store (r, c) id of the maximum point

        # 2-3. Update B_i,j
        for i in range(N):
            for j in range(N):
                gid = G[i][j]
                if (i == G_max_dict[gid][0]) and (j == G_max_dict[gid][1]):
                    B[i][j] += (len(G_dict[gid]) - 1)
                else:
                    B[i][j] -= 1
        
        # Step 3. Dinner
        # 3-1. Sort max. per f
        is_propagated = _init_group()
        G_max_dict_per_len_f = {}
        for gid in G_max_dict.keys():
            r, c = G_max_dict[gid][0], G_max_dict[gid][1]
            len_f = len(F[r][c])
            b = B[r][c]
            if not (len_f in G_max_dict_per_len_f):
                G_max_dict_per_len_f[len_f] = []
            G_max_dict_per_len_f[len_f].append((b, r, c))

        for len_f in [1, 2, 3]:
            if not (len_f in G_max_dict_per_len_f):
                continue
            gid_list = G_max_dict_per_len_f[len_f]
            gid_list.sort(key=lambda x: (-x[0], x[1], x[2]))
            for item in gid_list:
                i, j = item[1], item[2]
                gid = G[i][j]
                if (i == G_max_dict[gid][0]) and (j == G_max_dict[gid][1]) and (is_propagated[i][j] is None):
                    direction = B[i][j] % 4
                    B[i][j], x = 1, B[i][j] - 1
                    if direction == 0:
                        _propagate_up(i, j, B, F, is_propagated, x)
                    elif direction == 1:
                        _propagate_down(i, j, B, F, is_propagated, x)
                    elif direction == 2:
                        _propagate_left(i, j, B, F, is_propagated, x)
                    else:
                        _propagate_right(i, j, B, F, is_propagated, x)
                    # print(i, j)
                    # print(F)
                    # print(B)
                    # print('\n')
        CMT_cnt, CT_cnt, MT_cnt, CM_cnt, M_cnt, C_cnt, T_cnt = 0, 0, 0, 0, 0, 0, 0
        #print(F)
        for i in range(N):
            for j in range(N):
                if F[i][j] == "CMT":
                    CMT_cnt += B[i][j]
                elif F[i][j] == "CT":
                    CT_cnt += B[i][j]
                elif F[i][j] == "MT":
                    MT_cnt += B[i][j]
                elif F[i][j] == "CM":
                    CM_cnt += B[i][j]
                elif F[i][j] == "M":
                    M_cnt += B[i][j]
                elif F[i][j] == "C":
                    C_cnt += B[i][j]
                elif F[i][j] == "T":
                    T_cnt += B[i][j]
        print(f'{CMT_cnt} {CT_cnt} {MT_cnt} {CM_cnt} {M_cnt} {C_cnt} {T_cnt}')

if __name__ == '__main__':
    num = input().strip().split(' ')
    N, T = int(num[0]), int(num[1])
    F = []
    for i in range(N):
        F.append([])
        line = input().strip()
        for j in range(N):
            F[i].append(line[j])
    
    B = []
    for i in range(N):
        B.append([])
        line = input().strip().split(' ')
        for j in range(N):
            B[i].append(int(line[j]))

    run_simulation(N, T, F, B)