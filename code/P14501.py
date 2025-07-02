import sys
sys.setrecursionlimit(10**6)

def get_max(T_i, P_i, start, end):
    profit_max = 0
    for i in range(start, end):
        if i + T_i[i] <= end:
            cur_max = P_i[i] + get_max(T_i, P_i, start = i + T_i[i], end = end)
            profit_max = max(profit_max, cur_max)
    return profit_max

if __name__ == '__main__':
    N = int(input().strip())
    T_i, P_i = [], []
    for i in range(N):
        row = input().strip().split(' ')
        T_i.append(int(row[0]))
        P_i.append(int(row[1]))
    result = get_max(T_i, P_i, start = 0, end = N)
    print(result)