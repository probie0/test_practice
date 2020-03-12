class HandType:
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
# end def HandType


def get_card_value(card: str) -> int:
    str_value = card[0]
    value = None
    if str_value.isdigit():
        value = int(str_value)
    else:
        if str_value == 'T':
            value = 10
        elif str_value == 'J':
            value = 11
        elif str_value == 'Q':
            value = 12
        elif str_value == 'K':
            value = 13
        elif str_value == 'A':
            value = 14
    return value
# end def get_card_value()


def get_hand_type(cards: list) -> (HandType, list):
    values = [get_card_value(card) for card in cards]
    values.sort(reverse=True)
    colors = [card[1] for card in cards]
    comparing_values = list(set(values))
    comparing_values.sort(reverse=True)
    hand_type = HandType.HIGH_CARD
    is_flush = False
    if colors[0] == colors[1] == colors[2] == colors[3] == colors[4]:
        is_flush = True
    if len(comparing_values) == 5:
        if values[0] - values[1] == values[1] - values[2] == values[2] - values[3] == values[3] - values[4] == 1:
            if is_flush:
                hand_type = HandType.STRAIGHT_FLUSH
            else:
                hand_type = HandType.STRAIGHT
        else:
            if is_flush:
                hand_type = HandType.FLUSH
            else:
                hand_type = HandType.HIGH_CARD
    elif len(comparing_values) == 4:
        hand_type = HandType.PAIR
    elif len(comparing_values) == 3:
        if values[0] == values[1] == values[2] or values[1] == values[2] == values[3] or values[2] == values[3] == values[4]:
            hand_type = HandType.THREE_OF_A_KIND
        else:
            hand_type = HandType.TWO_PAIRS
    elif len(comparing_values) == 2:
        if values[0] == values[1] == values[2] == values[3] or values[1] == values[2] == values[3] == values[4]:
            hand_type = HandType.FOUR_OF_A_KIND
        else:
            hand_type = HandType.FULL_HOUSE

    return hand_type, comparing_values
# end def get_hand_type()


def compare(str_hand1: str, str_hand2: str) -> int:
    hand1 = str_hand1.split()
    hand2 = str_hand2.split()
    (type1, comparing_values1) = get_hand_type(hand1)
    (type2, comparing_values2) = get_hand_type(hand2)
    res = 0
    if type1 > type2:
        res = 1
    elif type1 < type2:
        res = -1
    else:
        for i in range(5):
            if comparing_values1[i] > comparing_values2[i]:
                res = 1
                break
            elif comparing_values1[i] < comparing_values2[i]:
                res = -1
                break
            else:
                continue
    return res
# end def compare
