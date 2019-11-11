import sys
import unittest
import importlib
import os
"""
Autograder for HW07 - CS1301 - Spring 2017
"""

class TestMyClass(unittest.TestCase):

    def test_char_count_1(self):
        self.assertEqual({}, hw.charCount(''), msg="Failed charCount w/ ''.")

    def test_char_count_2(self):
        self.assertEqual({'L':1,'o':1,'g':1,'a':1,'n':1}, hw.charCount('Logan'), msg="Failed charCount w/ 'Logan'.")

    def test_char_count_3(self):
        self.assertEqual({'A':1,'a':1,'B':1,'b':1,'C':1,'c':1}, hw.charCount('AaBbCc'), msg="Failed charCount w/ 'AaBbCc'.")

    def test_char_count_4(self):
        self.assertEqual({'t': 2, 'r': 2, 'c': 2, ' ': 8, 'a': 6, 'i': 2, 's': 2, '?': 1, 'w': 2, 'o': 1}, hw.charCount('was it a car or a cat i saw?'), msg="Failed charCount w/ 'was it a car or a cat i saw?'.")

    def test_char_count_5(self):
        self.assertEqual({'1':1,'2':1,'3':1,'4':1,'5':1,'^':1,'&':1,'*':1,'(':1,')':1}, hw.charCount('12345^&*()'), msg="Failed charCount w/ '12345^&*()'.")


    def test_shopping_1(self):
        self.assertEqual({'total': 0}, hw.shopping({},[]), msg="Failed shopping w/ {} and []")

    def test_shopping_2(self):
        self.assertEqual({'total': 0}, hw.shopping({},['cantaloupe']), msg="Failed shopping w/ {} and ['cantaloupe']")

    def test_shopping_3(self):
        self.assertEqual({'Banana': 5.94, 'total': 5.94}, hw.shopping({'Banana':(0.99,6)},[]), msg="Failed shopping w/ {'Banana':(0.99,6)} and []")

    def test_shopping_4(self):
        self.assertEqual({'total': 4.75, 'Banana': 4.75}, hw.shopping({'Banana':(0.99,6)},['banana']), msg="Failed shopping w/ {'Banana':(0.99,6)} and ['banana']")

    def test_shopping_5(self):
        self.assertEqual({'total': 21.2, 'Turkey': 4.78, 'Provolone': 5.91, 'Bread': 2.05, 'Salami': 5.52, 'Apple': 2.94}, hw.shopping({'Bread': (2.05,1), 'Provolone': (1.97,3), 'Salami': (3.45, 2), 'Turkey': (2.99, 2), 'Apple':(0.49, 6)},['salami','turkey']), msg="Failed shopping w/ {'Bread': (2.05,1), 'Provolone': (1.97,3), 'Salami': (3.45, 2), 'Turkey': (2.99, 2), 'Apple':(0.49, 6)} and ['Salami','Turkey']")


    def test_dict_replace_str_1(self):
        self.assertEqual('', hw.dictReplaceStr('',{}), msg="Failed dictReplaceStr w/ '' and {}.")

    def test_dict_replace_str_2(self):
        self.assertEqual('Hi', hw.dictReplaceStr('',{'':'Hi'}), msg="Failed dictReplaceStr w/ '' and {'':'Hi'}.")

    def test_dict_replace_str_3(self):
        self.assertEqual('laugh out loud, I will be right back as soon as possible. I love you', hw.dictReplaceStr('lol, I will brb asap. ily',{"brb": "be right back", "asap": "as soon as possible", "ily": "I love you", "lol":"laugh out loud"}), msg="Failed dictReplaceStr w/ 'lol, I will brb asap. ily' and {'brb': 'be right back', 'asap': 'as soon as possible', 'ily': 'I love you', 'lol':'laugh out loud'}.")

    def test_dict_replace_str_4(self):
        self.assertEqual('Logan', hw.dictReplaceStr('Logan',{'Wolverine': 'X-Men'}), msg="Failed dictReplaceStr w/ 'Logan' and {'Wolverine': 'X-Men'}.")

    def test_dict_replace_str_5(self):
        self.assertEqual('Movies Movies Movies Movies', hw.dictReplaceStr('   ',{'':'Movies'}), msg="Failed dictReplaceStr w/ '   ' and {'':'Movies'}.")


    def test_group_age_1(self):
        self.assertEqual({'AWA': 41, 'OutKast': 3042, 'Migos': 74, 'Michael Jackson': 50}, hw.groupAge({'AWA': {'Yung Coco Butter': 20, 'Yung Erica': 21}, 'OutKast': {'Big Boi': 42, 'Andre 3000': 3000}, 'Migos': {'Quavo': 25, 'Offset': 23, 'Takeoff': 26}, 'Michael Jackson': {'Michael': 50}}), msg="Failed groupAge w/ {'AWA': {'Yung Coco Butter': 20, 'Yung Erica': 21}, 'OutKast': {'Big Boi': 42, 'Andre 3000': 3000}, 'Migos': {'Quavo': 25, 'Offset': 23, 'Takeoff': 26}, 'Michael Jackson': {'Michael': 50}}.")

    def test_group_age_2(self):
        self.assertEqual({'AWA': 0, 'Migos': 0, 'OutKast': 0, 'Michael Jackson': 0}, hw.groupAge({'AWA': {}, 'OutKast': {}, 'Migos': {}, 'Michael Jackson': {}}), msg="Failed groupAge w/ {'AWA': {}, 'OutKast': {}, 'Migos': {}, 'Michael Jackson': {}}.")

    def test_group_age_3(self):
        self.assertEqual({'A': 48}, hw.groupAge({'A': {'b': 21, 'c': 21}, 'A': {'g': 25, 'h': 23}}), msg="Failed groupAge w/ {'A': {'b': 21, 'c': 21}, 'A': {'g': 25, 'h': 23}}.")

    def test_group_age_4(self):
        self.assertEqual({}, hw.groupAge({}), msg="Failed groupAge w/ {}.")

    def test_group_age_5(self):
        self.assertEqual({'G': -74, 'A': -20, 'D': -72}, hw.groupAge({'A': {'B': -20}, 'D': {'E': -42, 'F': -30}, 'G': {'H': -25, 'I': -23, 'J': -26}}), msg="Failed groupAge w/ {'A': {'B': -20}, 'D': {'E': -42, 'F': -30}, 'G': {'H': -25, 'I': -23, 'J': -26}}.")


    def test_statistics_1(self):
        self.assertEqual({'mode': sorted([0]), 'var': 0.0, 'sum': 0, 'median': 0, 'sdev': 0.0, 'min': 0, 'max': 0, 'mean': 0.0}, hw.statistics([0]), msg="Failed statistics w/ [0].")

    def test_statistics_2(self):
        self.assertEqual({'min': 29.558, 'sdev': 19.254, 'sum': 180.911, 'mean': 45.228, 'max': 78.188, 'median': 36.582, 'var': 370.701, 'mode': sorted([35.752, 29.558, 78.188, 37.413])}, hw.statistics([29.557853098027177, 78.18820699805177, 35.75183513220217, 37.41285122921468]), msg="Failed statistics w/ [29.557853098027177, 78.18820699805177, 35.75183513220217, 37.41285122921468].")

    def test_statistics_3(self):
        self.assertEqual({'min': 21, 'sdev': 14.445, 'sum': 333, 'mean': 37.0, 'max': 56, 'median': 34, 'var': 208.667, 'mode': sorted([56, 34, 21])}, hw.statistics([21, 21, 21, 34, 34, 34, 56, 56, 56]), msg="Failed statistics w/ [21, 21, 21, 34, 34, 34, 56, 56, 56].")

    def test_statistics_4(self):
        self.assertEqual({'min': 1, 'sdev': 12.0, 'sum': 130, 'mean': 13.0, 'max': 25, 'median': 13.0, 'var': 144.0, 'mode': sorted([1, 25])}, hw.statistics([25,1,25,1,25,1,25,1,25,1]), msg="Failed statistics w/ [25,1,25,1,25,1,25,1,25,1].")

    def test_statistics_5(self):
        self.assertEqual({'min': -791, 'sdev': 476.26, 'sum': 127.681, 'mean': 21.28, 'max': 846.7, 'median': -4.655, 'var': 226823.875, 'mode': sorted([3.689, 134.432, -791, -53.14, 846.7, -13])}, hw.statistics([-13, -53.14, 134.432, 846.7, -791, 3.689]), msg="Failed statistics w/ [-13, -53.14, 134.432, 846.7, -791, 3.689].")


if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW7")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW5.py or file is not in the same directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
