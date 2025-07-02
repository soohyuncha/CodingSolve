def get_max(map_2d, N, M):
    def _get_max_type_1(map_2d, N, M):
        result = 0
        # Case 1.
        # [- - - -]
        for i in range(N):
            for j in range(M - 3):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i][j + 2] + map_2d[i][j + 3]
                result = max(result, cur_sum)
        # Case 2.
        # [-]
        # [-]
        # [-]
        # [-]
        for j in range(M):
            for i in range(N - 3):
                cur_sum = map_2d[i][j] + map_2d[i + 1][j] + map_2d[i + 2][j] + map_2d[i + 3][j]
                result = max(result, cur_sum)
        return result
    
    def _get_max_type_2(map_2d, N, M):
        result = 0
        # [- -]
        # [- -]
        for i in range(N - 1):
            for j in range(M - 1):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i + 1][j] + map_2d[i + 1][j + 1]
                result = max(result, cur_sum)
        return result
    
    def _get_max_type_3(map_2d, N, M):
        result = 0
        # Case 1.
        # [-]
        # [-]
        # [-] [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j] + map_2d[i + 1][j] + map_2d[i + 2][j] + map_2d[i + 2][j + 1]
                result = max(result, cur_sum)
        # Case 2.
        # [-] [-] [-]
        # [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i][j + 2] + map_2d[i + 1][j]
                result = max(result, cur_sum)
        # Case 3.
        # [-] [-]
        #     [-]
        #     [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i + 1][j + 1] + map_2d[i + 2][j + 1]
                result = max(result, cur_sum)
        # Case 4.
        #         [-]
        # [-] [-] [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j + 2] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 1][j + 2]
                result = max(result, cur_sum)
        # Case 5. (Symmetry)
        #     [-]
        #     [-]
        # [-] [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j + 1] + map_2d[i + 1][j + 1] + map_2d[i + 2][j] + map_2d[i + 2][j + 1]
                result = max(result, cur_sum)
        # Case 6.
        # [-]
        # [-] [-] [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 1][j + 2]
                result = max(result, cur_sum)
        # Case 7.
        # [-] [-]
        # [-]
        # [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i + 1][j] + map_2d[i + 2][j]
                result = max(result, cur_sum)
        # Case 8.
        # [-] [-] [-]
        #         [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i][j + 2] + map_2d[i + 1][j + 2]
                result = max(result, cur_sum)

        return result
    
    def _get_max_type_4(map_2d, N, M):
        result = 0
        # Case 1.
        # [-]
        # [-] [-]
        #     [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 2][j + 1]
                result = max(result, cur_sum)
        # Case 2.
        #     [-] [-]
        # [-] [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j + 1] + map_2d[i][j + 2] + map_2d[i + 1][j] + map_2d[i + 1][j + 1]
                result = max(result, cur_sum)
        # Case 3. (Symmetry)
        #     [-]
        # [-] [-]
        # [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j + 1] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 2][j]
                result = max(result, cur_sum)
        # Case 4.
        # [-] [-]
        #     [-] [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i + 1][j + 1] + map_2d[i + 1][j + 2]
                result = max(result, cur_sum)
        return result
    
    def _get_max_type_5(map_2d, N, M):
        result = 0
        # Case 1.
        # [-] [-] [-]
        #     [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j] + map_2d[i][j + 1] + map_2d[i][j + 2] + map_2d[i + 1][j + 1]
                result = max(result, cur_sum)
        # Case 2.
        #     [-]
        # [-] [-]
        #     [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j + 1] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 2][j + 1]
                result = max(result, cur_sum)
        # Case 3.
        #     [-]
        # [-] [-] [-]
        for i in range(N - 1):
            for j in range(M - 2):
                cur_sum = map_2d[i][j + 1] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 1][j + 2]
                result = max(result, cur_sum)
        # Case 4.
        # [-]
        # [-] [-]
        # [-]
        for i in range(N - 2):
            for j in range(M - 1):
                cur_sum = map_2d[i][j] + map_2d[i + 1][j] + map_2d[i + 1][j + 1] + map_2d[i + 2][j]
                result = max(result, cur_sum)
        return result
    
    result = 0
    # Get max for each type of Tetromino
    result = max(result, _get_max_type_1(map_2d, N, M))
    result = max(result, _get_max_type_2(map_2d, N, M))
    result = max(result, _get_max_type_3(map_2d, N, M))
    result = max(result, _get_max_type_4(map_2d, N, M))
    result = max(result, _get_max_type_5(map_2d, N, M))
    return result


if __name__ == '__main__':
    N, M = input().strip().split(' ')
    N, M = int(N), int(M)
    map_2d = []
    for i in range(N):
        map_2d.append(input().strip().split(' '))
        for j in range(M):
            map_2d[i][j] = int(map_2d[i][j])
    
    result = get_max(map_2d, N, M)
    print(result)