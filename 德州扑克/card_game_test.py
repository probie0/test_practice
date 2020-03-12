import unittest
from parameterized import parameterized

from card_game import get_hand_type
from card_game import HandType
from card_game import compare


class CardTypeTest(unittest.TestCase):

    def test1(self):
        hand = '2H 3D 5S 9C KD'.split()
        handtype,_ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.HIGH_CARD)
    def test2(self):
        hand = '2C 3H 4S 8C AH'.split()
        handtype,_ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.HIGH_CARD)
    def test3(self):
        hand = '2H 4S 4C 2D 4H'.split()
        handtype,_ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.FULL_HOUSE)
    def test4(self):
        hand = '2H 3D 4S 5C 6D'.split()
        handtype,_ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.STRAIGHT)
    def test5(self):
        hand = '2H 3H 4H 5H 6H'.split()
        handtype,_ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.STRAIGHT_FLUSH)
    def test6(self):
        hand = '2H 3H 4H 5D 2H'.split()
        handtype, _ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.PAIR)
    def test7(self):
        hand = '2H 3H 3H 5D 2H'.split()
        handtype, _ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.TWO_PAIRS)
    def test8(self):
        hand = '2H 2H 2H QD 2H'.split()
        handtype, _ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.FOUR_OF_A_KIND)
    def test9(self):
        hand = '2H 2H 2H 5D JH'.split()
        handtype, _ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.THREE_OF_A_KIND)
    def test5(self):
        hand = '2H 8H 4H 5H 6H'.split()
        handtype,_ = get_hand_type(hand)
        self.assertEqual(handtype, HandType.FLUSH)



class CompareTest(unittest.TestCase):
    @parameterized.expand((
            ("2H 3D 5S 9C KD", "2C 3H 4S 8C AH", -1),
            ("2H 4S 4C 2D 4H", "2S 8S AS QS 3S", 1),
            ("2H 3D 5S 9C KD", "2C 3H 4S 8C KH", 1),
            ("2H 3D 5S 9C KD", "2D 3H 5C 9S KH", 0)
    ))
    def test(self, a, b, c):
        res = compare(a, b)
        self.assertEqual(res, c)


if __name__ == '__main__':
    unittest.main()
