def get_supervisor(A, B, C):
    primary, second = 0, 0
    for a in A:
        a = max(a - B, 0)
        primary += 1
        if a > 0:
            second += (a - 1) // C + 1
    return primary + second

if __name__ == '__main__':
    N = int(input())
    A = input().strip().split(' ')
    for i in range(len(A)):
        A[i] = int(A[i])
    B, C = input().strip().split(' ')
    B, C = int(B), int(C)

    print(get_supervisor(A, B, C))