def solution(n, k):
    def _is_prime(N):
        if N == 1:
            return False
        for i in range(2, N):
            if N % i == 0:
                return False
        return True
    def _is_type(num_str, i, j):
        if "0" in num_str[i:j+1]:
            return False
        if (i > 0) and (num_str[i-1] == "0") and (j < len(num_str) - 1) and (num_str[j+1] == "0"):
            return True
        if (i == 0) and (j < len(num_str) - 1) and (num_str[j+1] == "0"):
            return True
        if (i > 0) and (num_str[i-1] == "0") and (j == len(num_str) - 1):
            return True
        if (i == 0) and (j == len(num_str) - 1):
            return True
        return False
    N_MAX, K_MIN = 1000000, 3
    DIGIT_MAX = 1
    weight = K_MIN
    while 1:
        if weight >= N_MAX:
            break
        weight *= K_MIN
        DIGIT_MAX += 1
    
    k_radix = ""
    weight = k
    for power in range(DIGIT_MAX, -1, -1):
        q = n // (k**power)
        if q > 0:
            k_radix = k_radix + str(q)
            n = n % (k**power)
        elif len(k_radix) > 0:
            k_radix = k_radix + str(q)

    answer = 0
    for i in range(len(k_radix)):
        for j in range(i, len(k_radix)):
            if _is_type(k_radix, i, j) and _is_prime(int(k_radix[i:j+1])):
                answer += 1
    return answer

if __name__ == '__main__':
    n, k = 437674, 3
    ans = solution(n, k)
    print(ans)