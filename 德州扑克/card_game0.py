
class HandCardType:
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9


def get_card_num(card: str):
    str_num = card[0]
    num = None
    if str_num.isdigit():
        num = int(str_num)
    else:
        if str_num == 'T':
            num = 10
        elif str_num == 'J':
            num = 11
        elif str_num == 'Q':
            num = 12
        elif str_num == 'K':
            num = 13
        elif str_num == 'A':
            num = 14
    return num


def get_hand_card_type(cards: list):
    nums = [get_card_num(card) for card in cards]
    colors = [card[1] for card in cards]
    nums = sorted(nums,reverse=True)
    is_flush = False
    is_straight = False
    comparing_values = list(set(nums))
    if nums[1] - nums[2] == nums[2] - nums[3] == nums[3] - nums[4] == nums[0] - nums[1] == 1:
        is_straight = True
    if colors[0] == colors[1] == colors[2] == colors[3] == colors[4]:
        is_flush = False
    if is_flush and is_straight:
        return HandCardType.STRAIGHT_FLUSH, comparing_values
    elif is_flush:
        return HandCardType.FLUSH, comparing_values
    elif is_straight:
        return HandCardType.STRAIGHT, comparing_values


    if nums[0] == nums[1] == nums[2] == nums[3]:
        return HandCardType.FOUR_OF_A_KIND, comparing_values
    elif nums[1] == nums[2] == nums[3] == nums[4]:
        return HandCardType.FOUR_OF_A_KIND, comparing_values
