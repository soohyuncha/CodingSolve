def solution(numbers):
    def _dec_to_bin(number):
        return str(bin(number))[2:]
    
    def _to_full_binary_tree(binary_str):
        length = len(binary_str)
        log_len = 0
        while length > (2**log_len - 1):
            log_len += 1
        prefix_zero_len = 2**log_len - 1 - length
        return "0" * prefix_zero_len + binary_str
    
    def _valid_check(binary_str, is_root_zero):
        length = len(binary_str)
        # Base case;
        if length == 0:
            return True
        
        # Parent is already zero, but "1" in children node => invalid
        if is_root_zero and binary_str[length // 2] == '1':
            return False
        
        # Check left subtree
        if not _valid_check(binary_str[:length//2], binary_str[length // 2] == '0') :
            return False
        # Check right subtree
        if not _valid_check(binary_str[length//2 + 1:], binary_str[length // 2] == '0') :
            return False
        return True
    
    answer = []
    for number in numbers:
        binary_str = _dec_to_bin(number)
        full_binary_str = _to_full_binary_tree(binary_str)

        root_idx = len(full_binary_str) // 2
        if _valid_check(full_binary_str, full_binary_str[root_idx] == "0"):
            answer.append(1)
        else:
            answer.append(0)

    return answer

if __name__ == '__main__':
    numbers = [7, 42, 5]

    ans = solution(numbers)
    print(ans)