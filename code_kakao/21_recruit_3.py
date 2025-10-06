def solution(info, query):
    from bisect import bisect_left
    const_dict = {"cpp": 0, "java": 1, "python": 2, "backend": 0, "frontend": 1, "junior": 0, "senior": 1, "chicken": 0, "pizza": 1}

    # 1) Add info
    encoded_dict = {}
    for app in info:
        app_list = app.split(" ")
        encoded_val = const_dict[app_list[0]] * 8 + const_dict[app_list[1]] * 4 + const_dict[app_list[2]] * 2 + const_dict[app_list[3]] * 1
        if not (encoded_val in encoded_dict):
            encoded_dict[encoded_val] = []
        encoded_dict[encoded_val].append(int(app_list[4]))

    # 2) Sort
    for k in encoded_dict.keys():
        encoded_dict[k].sort()
    #print(encoded_dict)

    # 3) Process query
    answer = []
    for q in query:
        q_list = q.split(" ")
        # Field 1
        if q_list[0] == "-":
            key = [0, 8, 16]
        else:
            key = [const_dict[q_list[0]] * 8]
        # Field 2
        len_key = len(key)
        if q_list[2] == "-":
            for i in range(len_key):
                key.append(key[i] + 4)
        else:
            for i in range(len_key):
                key[i] += const_dict[q_list[2]] * 4
        # Field 3
        len_key = len(key)
        if q_list[4] == "-":
            for i in range(len_key):
                key.append(key[i] + 2)
        else:
            for i in range(len_key):
                key[i] += const_dict[q_list[4]] * 2
        # Field 4
        len_key = len(key)
        if q_list[6] == "-":
            for i in range(len_key):
                key.append(key[i] + 1)
        else:
            for i in range(len_key):
                key[i] += const_dict[q_list[6]] * 1

        thr = int(q_list[7])
        thr_cnt = 0
        for k in key:
            if not (k in encoded_dict) or len(encoded_dict[k]) == 0:
                continue
            l = bisect_left(encoded_dict[k], thr, 0)
            thr_cnt += len(encoded_dict[k]) - l
        answer.append(thr_cnt)

    return answer

if __name__ == '__main__':
    from bisect import *
    print(bisect_left([0, 1, 2, 2, 3, 3, 4], 3, 0))
    print(bisect_right([0, 1, 2, 2, 3, 3, 4], 3, 0))
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    result = solution(info, query)
    print(result)