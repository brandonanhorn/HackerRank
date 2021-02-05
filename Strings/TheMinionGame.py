def minion_game(string):
    vowels = 'AEIOU'
    str_lenght = len(string)
    first_score, second_score = 0, 0

    for i in range(str_lenght):
        if s[i] in vowels:
            first_score += (str_lenght - i)
        else:
            second_score += (str_lenght - i)

    if first_score > second_score:
        print("Kevin", first_score)
    elif first_score < second_score:
        print("Stuart", second_score)
    else:
        print("Draw")
