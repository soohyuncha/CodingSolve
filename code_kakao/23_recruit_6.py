def solution(n, m, x, y, r, c, k):
    def _dfs(r_cur, c_cur, remaining_dist, history):
        if history:
            if (r_cur == r_goal) and (c_cur == c_goal) and (remaining_dist == 0):
                return history
            if (r_cur >= n) or (r_cur < 0) or (c_cur >= m) or (c_cur < 0) :
                return None
            # Terminate immediately; Prune the subsequent unnecessary searching paths
            minimum_dist = abs(r_cur - r_goal) + abs(c_cur - c_goal)
            if (remaining_dist < minimum_dist) or (remaining_dist % 2 != minimum_dist % 2):
                return None
            
        # d (Down)
        if r_cur < n - 1:
            answer = _dfs(r_cur + 1, c_cur, remaining_dist=remaining_dist-1, history=history+"d")
            if answer is not None:
                return answer
        # l (Left)
        if c_cur > 0 :
            answer = _dfs(r_cur, c_cur - 1, remaining_dist=remaining_dist-1, history=history+"l")
            if answer is not None:
                return answer
        # r (Right)
        if c_cur < m - 1:
            answer = _dfs(r_cur, c_cur + 1, remaining_dist=remaining_dist-1, history=history+"r")
            if answer is not None:
                return answer
        # u (Up)
        if r_cur > 0:
            answer = _dfs(r_cur - 1, c_cur, remaining_dist=remaining_dist-1, history=history+"u")
            if answer is not None:
                return answer
        return None

    import sys
    sys.setrecursionlimit(10**6)
    r_goal, c_goal = r - 1, c - 1
    r_cur, c_cur = x - 1, y - 1
    answer = _dfs(r_cur, c_cur, remaining_dist=k, history="")
    answer = answer if answer is not None else "impossible"
    return answer


if __name__ == '__main__':
    n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5

    ans = solution(n, m, x, y, r, c, k)
    print(ans)