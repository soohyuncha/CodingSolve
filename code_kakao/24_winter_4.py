# def solution(coin, cards):
#     def _round(coin, cards_mine, cards_remaining, turn):
#         # No cards left
#         if len(cards_remaining) == 0:
#             return turn + 1     # Return the "reached" turn; Not a "completed" turn
#         card_1, card_2 = cards_remaining[:2]

#         case_1_best, case_2_best, case_3_best, case_4_best = turn + 1, turn + 1, turn + 1, turn + 1

#         # Determine whether the new cards are useful
#         card_1_pair = n - card_1
#         card_2_pair = n - card_2

#         # Case 1. Get both
#         if coin >= 2:
#             card_1_useful = (card_1_pair in cards_mine) or (card_1_pair == card_2) or (card_1_pair in cards_remaining[2:2+(coin-2)*2])
#             card_2_useful = (card_2_pair in cards_mine) or (card_2_pair == card_1) or (card_2_pair in cards_remaining[2:2+(coin-2)*2])
#             if card_1_useful and card_2_useful:
#                 cards_mine_updated = cards_mine + [card_1, card_2]
#                 find_pair = False
#                 for i in range(len(cards_mine_updated)):
#                     for j in range(i + 1, len(cards_mine_updated)):
#                         if cards_mine_updated[i] + cards_mine_updated[j] == n :
#                             ans = _round(coin - 2, cards_mine=cards_mine_updated[:i] + cards_mine_updated[i+1:j] + cards_mine_updated[j+1:], cards_remaining=cards_remaining[2:], turn=turn+1)
#                             case_1_best = max(case_1_best, ans)
#                             find_pair = True
#                         if find_pair:
#                             break
#                     if find_pair:
#                         break

#         # Case 2. Get 1st card
#         if coin >= 1 :
#             card_1_useful = (card_1_pair in cards_mine) or (card_1_pair == card_2) or (card_1_pair in cards_remaining[2:2+(coin-1)*2])
#             if card_1_useful:
#                 cards_mine_updated = cards_mine + [card_1]
#                 find_pair = False
#                 for i in range(len(cards_mine_updated)):
#                     for j in range(i + 1, len(cards_mine_updated)):
#                         if cards_mine_updated[i] + cards_mine_updated[j] == n :
#                             ans = _round(coin - 1, cards_mine=cards_mine_updated[:i] + cards_mine_updated[i+1:j] + cards_mine_updated[j+1:], cards_remaining=cards_remaining[2:], turn=turn+1)
#                             case_2_best = max(case_2_best, ans)
#                             find_pair = True
#                         if find_pair:
#                             break
#                     if find_pair:
#                         break

#         # Case 3. Get 2nd card
#         if coin >= 1 :
#             card_2_useful = (card_2_pair in cards_mine) or (card_2_pair == card_1) or (card_2_pair in cards_remaining[2:2+(coin-1)*2])
#             if card_2_useful:
#                 cards_mine_updated = cards_mine + [card_2]
#                 find_pair = False
#                 for i in range(len(cards_mine_updated)):
#                     for j in range(i + 1, len(cards_mine_updated)):
#                         if cards_mine_updated[i] + cards_mine_updated[j] == n :
#                             ans = _round(coin - 1, cards_mine=cards_mine_updated[:i] + cards_mine_updated[i+1:j] + cards_mine_updated[j+1:], cards_remaining=cards_remaining[2:], turn=turn+1)
#                             case_3_best = max(case_3_best, ans)
#                             find_pair = True
#                         if find_pair:
#                             break
#                     if find_pair:
#                         break

#         # Case 4. Discard both
#         cards_mine_updated = cards_mine
#         find_pair = False
#         for i in range(len(cards_mine_updated)):
#             for j in range(i + 1, len(cards_mine_updated)):
#                 if cards_mine_updated[i] + cards_mine_updated[j] == n :
#                     ans = _round(coin, cards_mine=cards_mine_updated[:i] + cards_mine_updated[i+1:j] + cards_mine_updated[j+1:], cards_remaining=cards_remaining[2:], turn=turn+1)
#                     case_4_best = max(case_4_best, ans)
#                     find_pair = True
#                 if find_pair:
#                     break
#             if find_pair:
#                 break

#         return max(max(case_1_best, case_2_best), max(case_3_best, case_4_best))

#     n = len(cards) + 1
#     answer = _round(coin, cards_mine=cards[:len(cards)//3], cards_remaining=cards[len(cards)//3:], turn=0)
#     return answer

def solution(coin, cards):
    n = len(cards) + 1
    round_max = len(cards) // 3

    pair_priority_queue = []
    for i in range(len(cards)):
        pair_index = cards.index(n - cards[i])
        if i > pair_index:
            required_coins = (i >= len(cards)//3) + (pair_index >= len(cards)//3)
            required_turns_i = max(0, i - len(cards)//3) // 2
            required_turns_pair = max(0, pair_index - len(cards)//3) // 2
            required_turns = max(required_turns_i, required_turns_pair)
            pair_priority_queue.append([required_coins, required_turns])
    # We should use minimum coin
    pair_priority_queue.sort(key=lambda x: (x[0], x[1]))

    turn = 0
    while len(pair_priority_queue) > 0:
        selected_pair = None
        for i in range(len(pair_priority_queue)):
            pair = pair_priority_queue[i]
            # Required coin should be less than our coint
            # Required turn should be less than our turn
            if pair[0] <= coin and pair[1] <= turn:
                selected_pair = pair_priority_queue.pop(i)
                break
        
        if selected_pair is None or (turn == round_max):
            return turn + 1

        coin -= selected_pair[0]
        turn += 1
            

if __name__ == '__main__':
    #coin, cards = 4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
    #coin, cards = 3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
    coin, cards = 2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
    
    ans = solution(coin, cards)
    print(ans)