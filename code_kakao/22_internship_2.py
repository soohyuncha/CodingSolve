# def solution(queue1, queue2):
#     queue_len = len(queue1)
#     queue_sum = sum(queue1) + sum(queue2)
#     if queue_sum % 2 == 1:
#         return -1
#     equal_sum = queue_sum // 2
#     circular_queue = queue1 + queue2
#     ans = []
#     queue1_sum_base = sum(circular_queue[:queue_len])
#     for i in range(queue_len):
#         # Reuse "queue1_sum"
#         queue1_sum = queue1_sum_base
#         for j in range(queue_len, 2 * queue_len):
#             #print(i, j, queue1_sum)
#             if queue1_sum == equal_sum:
#                 ans.append(i + j - queue_len)
#             queue1_sum += circular_queue[j]
#         for j in range(i):
#             #print(i, j, queue1_sum)
#             if queue1_sum == equal_sum:
#                 ans.append(i + j + queue_len)
#             queue1_sum += circular_queue[j]
#         queue1_sum_base -= circular_queue[i]

#     for i in range(queue_len, 2*queue_len):
#         # Reuse "queue1_sum"
#         queue1_sum = circular_queue[i]
#         for j in range(i + 1, 2 * queue_len):
#             #print(i, j, queue1_sum)
#             if queue1_sum == equal_sum:
#                 ans.append(i + j - queue_len)
#             queue1_sum += circular_queue[j]
#     return min(ans) if len(ans) > 0 else -1


# def solution(queue1, queue2):
#     queue_len = len(queue1)
#     queue_sum = sum(queue1) + sum(queue2)
#     if queue_sum % 2 == 1:
#         return -1
#     equal_sum = queue_sum // 2
#     circular_queue = queue1 + queue2
#     ans = []

#     for i in range(2 * queue_len):
#         acc = circular_queue[i]
#         for j in range(i + 1, 2 * queue_len):
#             if acc > equal_sum:
#                 break
#             if acc == equal_sum:
#                 queue1_shift = i
#                 queue2_shift = (j - queue_len) if j >= queue_len else j + queue_len
#                 ans.append(queue1_shift + queue2_shift)
#             acc += circular_queue[j]

#     return min(ans) if len(ans) > 0 else -1

def solution(queue1, queue2):
    from collections import deque
    queue1, queue2 = deque(queue1), deque(queue2)
    queue_len = len(queue1)
    queue_sum1, queue_sum2 = sum(queue1), sum(queue2)
    queue_sum = queue_sum1 + queue_sum2
    if queue_sum % 2 == 1:
        return -1
    equal_sum = queue_sum // 2
    
    turn = 0
    while turn < 3 * queue_len:
        if queue_sum2 == equal_sum:
            return turn
        # queue 2 -> 1
        elif queue_sum2 > equal_sum:
            queue_sum1 += queue2[0]
            queue_sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        # queue 1 -> 2
        else:
            queue_sum1 -= queue1[0]
            queue_sum2 += queue1[0]
            queue2.append(queue1.popleft())
        turn += 1
    return -1

if __name__ == '__main__':
#    queue1, queue2 = [3, 2, 7, 2], [4, 6, 5, 1]
#    queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]
    queue1, queue2 = [1, 10, 1, 2], [1, 2, 1, 2]
    queue1, queue2 = [1, 1, 1, 1], [1, 1, 7, 1]
    ans = solution(queue1, queue2)
    print(ans)