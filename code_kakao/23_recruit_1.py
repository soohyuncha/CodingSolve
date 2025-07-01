def solution(today, terms, privacies):
    # today (y/m/d) into absolute date
    y, m, d = int(today[:4]) - 2000, int(today[5:7]), int(today[8:])
    today_date = y * 12 * 28 + m * 28 + d

    # "terms_dict"
    # key: term, value: days
    terms_dict = {}
    for term in terms:
        term_id, month = term.split(' ')
        terms_dict[term_id] = int(month) * 28

    # Get answer by comparing expiry date to today for each privacy
    answer = []
    idx = 1
    for privacy in privacies:
        date, term_id = privacy.split(' ')
        y, m, d = int(date[:4]) - 2000, int(date[5:7]), int(date[8:])
        expiry_date = (y * 12 * 28 + m * 28 + d) + terms_dict[term_id]
        if expiry_date <= today_date:
            answer.append(idx)
        idx += 1

    return answer

if __name__ == '__main__':
    today_1 = "2022.05.19"
    terms_1 = ["A 6", "B 12", "C 3"]
    privacies_1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    today_2 = "2020.01.01"
    terms_2 = ["Z 3", "D 5"]
    privacies_2 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    print(solution(today_2, terms_2, privacies_2))