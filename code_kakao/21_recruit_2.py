def solution(orders, course):
    def _get_combination(substitute, combination, len_string, combination_list):
        if len(combination) == len_string:
            combination_list.append(''.join(sorted(combination)))
            return
        for idx, s in enumerate(substitute):
            _get_combination(substitute[idx+1:], combination + s, len_string, combination_list)

    combination_freq = {}
    for order in orders:
        for c in course:
            # Search combination
            combination_list = []
            _get_combination(order, "", c, combination_list)
            # Add in list
            if not c in combination_freq:
                combination_freq[c] = {}
            for combination in combination_list:
                if not (combination in combination_freq[c]):
                    combination_freq[c][combination] = 0
                combination_freq[c][combination] += 1
    answer = []
    for c in course:
        max_freq = 0
        for combination in combination_freq[c].keys():
            max_freq = max(max_freq, combination_freq[c][combination])
        for combination in combination_freq[c].keys():
            if max_freq > 1 and combination_freq[c][combination] == max_freq:
                answer.append(combination)
    answer.sort()
    return answer

if __name__ == '__main__':
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    result = solution(orders, course)
    print(result)