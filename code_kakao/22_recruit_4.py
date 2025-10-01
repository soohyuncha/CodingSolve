def solution(n, info):
    def _find_solution(idx, n, L):
        # Base case; n == 0
        if n == 0:
            while len(L) != len(info):
                L.append(0)

            app, lion = 0, 0
            for i in range(len(L)):
                if info[i] > 0 and info[i] >= L[i]:
                    app += (10-i)
                elif L[i] > 0:
                    lion += (10-i)
            if lion > app:
                return (lion - app, L)
            return None
        
        # Two possible cases
        answer_with_zero, answer_with_more = None, None
        if idx < len(info) - 1:
            answer_with_zero = _find_solution(idx + 1, n, L + [0])
        if idx == len(info) - 1:
            answer_with_more = _find_solution(idx + 1, 0, L + [n])
        elif n > info[idx]:
            answer_with_more = _find_solution(idx + 1, n - (info[idx] + 1), L + [info[idx] + 1])
        
        # Select one of the best answer
        if answer_with_zero is None:
            return answer_with_more
        if answer_with_more is None:
            return answer_with_zero
        if answer_with_zero[0] > answer_with_more[0]:
            return answer_with_zero
        if answer_with_zero[0] < answer_with_more[0]:
            return answer_with_more
        for i in range(len(info) - 1, -1, -1):
            if answer_with_more[1][i] > answer_with_zero[1][i]:
                return answer_with_more
            if answer_with_zero[1][i] > answer_with_more[1][i]:
                return answer_with_zero
        
    answer = _find_solution(0, n, [])
    if answer is None:
        return [-1]
    
    return answer[1]

if __name__ == '__main__':
    n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]

    result = solution(n, info)
    print(result)