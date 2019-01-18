def poker_hand_score(hand):
    # e.g. Hand: "5H KS 9C 7D 9H"
    import collections

    def straight_hand(c_values):
        c_values = sorted(c_values)
        for i in range(1, len(c_values)):
            if int(c_values[i-1]) - int(c_values[i]) != -1:
                return False
        return True


    list_cards = hand.split(" ")

    card_values = sorted([i[0] for i in list_cards])

    dict_old_to_new_values = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}

    new_card_values = []

    for n in card_values:
        if n in dict_old_to_new_values:
            new_card_values.append(int(dict_old_to_new_values[n]))
        else:
            new_card_values.append(int(n))

    card_suits = [i[1] for i in list_cards]

    # if hand is royal flush return score of 10
    if new_card_values == ['T', 'J', 'Q', 'K', 'A'] and len(set(card_suits)) == 1:
        print(hand)
        return 1000

    # if hand is straight flush return 9
    if straight_hand(new_card_values) and len(set(card_suits)) == 1:
        print(hand)
        return 900

    # if hand is 4 of a kind return 8
    if collections.Counter(new_card_values).most_common(1)[0][1] == 4:
        print(hand)
        return 800

    # if hand is a full house return 7
    hand_counter = collections.Counter(new_card_values).most_common(5)

    if hand_counter[0][1] == 3 and hand_counter[1][1] == 2:
        print(hand)
        return 700

    # if hand is a flush return 6
    if len(set(card_suits)) == 1:
        print(hand)
        return 600

    # if hand is a straight return 5
    if straight_hand(new_card_values):
        return 500

    # if hand is 3 of a kind return 4
    if hand_counter[0][1] == 3:
        return 400

    # if hand is 2 pair return 3
    if hand_counter[0][1] == 2 and hand_counter[1][1] == 2:
        return 300

    if hand_counter[0][1] == 2:
        value_of_pair = (hand_counter[0][0])
        return 200 + value_of_pair

    if hand_counter[0][1] == 1:
        value_to_return = 1 + (max(new_card_values))
        return value_to_return

    else:
        return ("ERROR", list_cards, hand)



f = open('p054_poker.txt')

hands_won_by_1 = 0

hands_won_by_2 = 0

manual_solve = 0

for line in f:
    hand_1 = line[0:14]
    hand_2 = line[15:29]
    p1_score = poker_hand_score(hand_1)
    p2_score = poker_hand_score(hand_2)
    if p1_score > p2_score:
        hands_won_by_1 += 1
        print("1 WIN!", hand_1, p1_score, hand_2, p2_score)

    elif p2_score > p1_score:
        hands_won_by_2 += 1
        print("2 WIN!", hand_1, p1_score, hand_2, p2_score)

    elif p1_score == p2_score:
        print(hand_1, hand_2)
        manual_solve += 1

print(hands_won_by_1)

print(hands_won_by_2)

print(manual_solve)