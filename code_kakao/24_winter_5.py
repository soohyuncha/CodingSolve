import sys
sys.setrecursionlimit(10**6)

# def solution(n, tops):
#     def _dfs(idx, type):
#         # type 0: original triangle
#         if type == 0:
#             # Base case
#             if idx == n:
#                 return 1
#             triangle = _dfs(idx, type=1)
#             diamond = _dfs(idx + 1, type=0)
#             return triangle + diamond
#         # type 1: reversed triangle; check whether top triangle exists
#         elif type == 1:
#             if idx == n-1:
#                 if tops[idx] == 1:
#                     return 3
#                 else:
#                     return 2
#             triangle = _dfs(idx + 1, type=0)
#             diamond = _dfs(idx + 1, type=1)
#             if tops[idx] == 1:
#                 return 2*triangle + diamond
#             else:
#                 return triangle + diamond

#     answer = _dfs(idx=0, type=0)
#     return answer % 10007

def solution(n, tops):
    single, diamond = 0, 0
    for i in range(n):
        for j in range(2):
            # Init
            if (i == 0) and (j == 0):
                single, diamond = 1, 0
            elif j == 0:
                single, diamond = single + diamond, single
            else:
                single, diamond = single + diamond, single + (single + diamond) * tops[i]
    single, diamond = single + diamond, single
    return (single + diamond) % 10007


if __name__ == '__main__':
    n, tops = 4, [1, 1, 0, 1]
#    n, tops = 2, [0, 1]
    ans = solution(n, tops)
    print(ans)