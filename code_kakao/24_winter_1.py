def solution(friends, gifts):
    # Store "gift history"; [sender][receiver]
    gift_history = {}
    for f in friends:
        gift_history[f] = {}
        for ff in friends:
            if f != ff :
                gift_history[f][ff] = 0
    
    for gift in gifts:
        sender, receiver = gift.split(' ')
        gift_history[sender][receiver] += 1
    
    # Compute "gift score"; #. send - #. receive
    gift_score = {}
    for f in friends:
        send, receive = 0, 0
        for ff in friends:
            if f != ff:
                send += gift_history[f][ff]
                receive += gift_history[ff][f]
        gift_score[f] = send - receive
    
    # Get answer by comparing each pair of friends
    gift_next = {}
    for f in friends:
        gift_next[f] = 0
    for i in range(len(friends)):
        f = friends[i]
        for j in range(i + 1, len(friends)):
            ff = friends[j]
            if f == ff:
                continue
            if (gift_history[f][ff] == 0 and gift_history[ff][f] == 0) or (gift_history[f][ff] == gift_history[ff][f]):
                if gift_score[f] > gift_score[ff]:
                    gift_next[f] += 1
                elif gift_score[f] < gift_score[ff]:
                    gift_next[ff] += 1
            else:
                if gift_history[f][ff] > gift_history[ff][f]:
                    gift_next[f] += 1
                else:
                    gift_next[ff] += 1
    answer = 0
    for f in gift_next.keys():
        answer = max(answer, gift_next[f])
    return answer

if __name__ == '__main__':
    friends_1 = ["muzi", "ryan", "frodo", "neo"]
    gifts_1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    friends_2 = ["joy", "brad", "alessandro", "conan", "david"]
    gifts_2 = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
    friends_3 = ["a", "b", "c"]
    gifts_3 = ["a b", "b a", "c a", "a c", "a c", "c a"]	
    print(solution(friends_3, gifts_3))