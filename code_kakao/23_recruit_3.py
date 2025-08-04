def solution(users, emoticons):
    def _find_best_dfs(emoticons, emoticons_sales_ratio, emoticons_sales_price):
        # Base case; find maximum by iterating over "users"
        if len(emoticons) == 0:
            num_members, total_money = 0, 0
            for user in users:
                user_sum = 0
                for i, e_sales_ratio in enumerate(emoticons_sales_ratio):
                    if e_sales_ratio >= user[0] * 0.01:
                        user_sum += emoticons_sales_price[i]
                if user_sum >= user[1]:
                    num_members += 1
                else:
                    total_money += user_sum
            #print(emoticons_sales_ratio, emoticons_sales_price, num_members, total_money)
            return num_members, total_money

        # Search over all "emoticon" in "emoticons"
        num_members_best, money_best = 0, 0
        emoticon = emoticons.pop(0)
        for sales_ratio in [0.1, 0.2, 0.3, 0.4]:
            emoticons_sales_ratio.append(sales_ratio)
            emoticons_sales_price.append(emoticon * (1-sales_ratio))
            num_members, money = _find_best_dfs(emoticons, emoticons_sales_ratio, emoticons_sales_price)
            emoticons_sales_ratio.pop(-1)
            emoticons_sales_price.pop(-1)

            # Update current best
            if num_members > num_members_best:
                num_members_best, money_best = num_members, money
            elif (num_members == num_members_best) and (money > money_best):
                money_best = money
        emoticons.insert(0, emoticon)
        return (num_members_best, int(money_best))            

    return _find_best_dfs(emoticons, [], [])

if __name__ == '__main__':
    # users = [[40, 10000], [25, 10000]]
    # emoticons = [7000, 9000]

    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]

    L = [1, 2, 3, 4,5]

    ans = solution(users, emoticons)
    print(ans)