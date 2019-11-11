import sys
import unittest
import importlib
import os
"""
Autograder for HW05 - CS1301 - Spring 2017
"""

class TestMyClass(unittest.TestCase):



    def test_complex_calculator_1(self):
        self.assertEqual(None, hw.complex_calculator('code', [1, 2, 3]), msg="Failed complex_calculator w/ 'code' and [1, 2, 3].")


    def test_complex_calculator_2(self):
        self.assertEqual(8.0, hw.complex_calculator('pow', [2, 3]), msg="Failed complex_calculator w/ 'pow' and [2, 3].")


    def test_complex_calculator_3(self):
        self.assertEqual(5.0, hw.complex_calculator('hypot', [3, 4]), msg="Failed complex_calculator w/ 'hypot' and [3, 4].")


    def test_complex_calculator_4(self):
        self.assertEqual(192.0, hw.complex_calculator('fabs', [-192]), msg="Failed complex_calculator w/ 'fabs' and [-192].")


    def test_complex_calculator_5(self):
        self.assertEqual(5, hw.complex_calculator('gcd', [125, 1940]), msg="Failed complex_calculator w/ 'gcd' and [125, 1940].")


    def test_complex_calculator_6(self):
        self.assertEqual(22, hw.complex_calculator('ceil', [21.2]), msg="Failed complex_calculator w/ 'ceil' and [21.2].")


    def test_extract_information_1(self):
        self.assertEqual(('NAME', 0, 'SCHOOL'), hw.extract_information('NAME: 0, SCHOOL'), msg="Failed extract_information w/ 'NAME: 0, SCHOOL'")


    def test_extract_information_2(self):
        self.assertEqual(('First Middle Last', 100, 'Elementory Middle High'), hw.extract_information('First Middle Last: 100 , Elementory Middle High'), msg="Failed extract_information w/ 'First Middle Last: 100 , Elementory Middle High")


    def test_extract_information_3(self):
        self.assertEqual(('Spongebob Squarepants', 19, 'Bikini Bottom Boating school'), hw.extract_information('Spongebob Squarepants: 19, Bikini Bottom Boating school'), msg="Failed extract_information w/ 'Spongebob Squarepants: 19, Bikini Bottom Boating school'")


    def test_extract_information_4(self):
        self.assertEqual(('Sarah Wilson', 12, 'Riverside Middle School'), hw.extract_information('Sarah Wilson: 12, Riverside Middle School'), msg="Failed extract_information w/ 'Sarah Wilson: 12, Riverside Middle School'")


    def test_extract_information_5(self):
        self.assertEqual(('Ellen D.', 57, 'Hollywood University'), hw.extract_information('Ellen D.: 57, Hollywood University'), msg="Failed extract_information w/ 'Ellen D.: 57, Hollywood University'")


    def test_create_addressbook_1(self):
        self.assertEqual([('High School', 'Adrienne', 18), ('Bikini Bottom Boating school', 'Spongebob Squarepants', 19), ('Hawkins Middle School', 'Eleven', 13), ('Georgia Tech', 'David', 21)], hw.create_addressbook(['Adrienne: 18, High School', 'Spongebob Squarepants: 19, Bikini Bottom Boating school', 'Eleven: 13, Hawkins Middle School', 'David: 21, Georgia Tech']), msg="Failed create_addressbook w/ ['Adrienne: 18, High School', 'Spongebob Squarepants: 19, Bikini Bottom Boating school', 'Eleven: 13, Hawkins Middle School', 'David: 21, Georgia Tech'].")


    def test_create_addressbook_2(self):
        self.assertEqual([('Hollywood University', 'Ellen D.', 57), ('SCHOOL', 'NAME', 0), ('Riverside Middle School', 'Sarah Wilson', 12), ('Lincoln Elementary School', 'Anton', 7)], hw.create_addressbook(['Ellen D.: 57, Hollywood University', 'NAME: 0, SCHOOL', 'Sarah Wilson: 12, Riverside Middle School', 'Anton: 56, Georgia Tech', 'Anton: 07, Lincoln Elementary School']), msg="Failed create_addressbook w/ ['Ellen D.: 57, Hollywood University', 'NAME: 0, SCHOOL', 'Sarah Wilson: 12, Riverside Middle School', 'Anton: 56, Georgia Tech', 'Anton: 07, Lincoln Elementary School'].")


    def test_create_addressbook_3(self):
        self.assertEqual([], hw.create_addressbook([]), msg="Failed create_addressbook w/ [].")


    def test_create_addressbook_4(self):
        self.assertEqual([('BC', 'William', 14)], hw.create_addressbook(['William: 14, BC']), msg="Failed create_addressbook w/ ['William: 14, BC'].")


    def test_create_addressbook_5(self):
        self.assertEqual([('Clemson', 'Baker', 17), ('Lakeside Elementary', 'Fred', 5), ('Rockburn Middle', 'Neal', 13)], hw.create_addressbook(['Neal: 21, UVA', 'Fred: 19, Cal Tech', 'Baker: 17, Clemson', 'Neal: 20, UWA', 'Fred: 5, Lakeside Elementary', 'Neal: 13, Rockburn Middle']), msg="Failed create_addressbook w/ ['Neal: 21, UVA', 'Fred: 19, Cal Tech', 'Baker: 17, Clemson', 'Neal: 20, UWA', 'Fred: 5, Lakeside Elementary', 'Neal: 13, Rockburn Middle'].")


    def test_get_averages_1(self):
        self.assertEqual([(2.0, 4.0, 6.0), (), (4.0, 4.0, 4.0)], hw.get_averages([(1,2,3), (), (2,2,2)]), msg="Failed get_averages w/ [(1,2,3), (), (2,2,2)].")


    def test_get_averages_2(self):
        self.assertEqual([(17.08, 47.83, 75.17), (24.0, 48.0), (1.0, 1.0, 1.0, 1.0, 1.0), (45.0, 5.0)], hw.get_averages([(2.5, 7, 11), (4,8), (1,1,1,1,1), (9,1)]), msg="Failed get_averages w/ [(2.5, 7, 11), (4,8), (1,1,1,1,1), (9,1)].")


    def test_get_averages_3(self):
        self.assertEqual([(), (), ()], hw.get_averages([(), (), ()]), msg="Failed get_averages w/ [(), (), ()].")


    def test_get_averages_4(self):
        self.assertEqual([(7.9, 19.75, 35.55, 11.85, 1.97, 16.59)], hw.get_averages([(2,5,9,3,.5,4.2)]), msg="Failed get_averages w/ [(2,5,9,3,.5,4.2)].")


    def test_get_averages_5(self):
        self.assertEqual([(3.25, 6.5, 9.75, 22.75), (41.33, 62.0, 217.0), (36.0,)], hw.get_averages([(1,2,3,7), (4,6,21), (6,)]), msg="Failed get_averages w/ [(1,2,3,7), (4,6,21), (6,)].")


    def test_party_time_1(self):
        self.assertEqual(('David', 'Karoline'), hw.party_time([('David', 4), ('Karoline', 4)], 6), msg="Failed party_time w/ [('David', 4), ('Karoline', 4)] and 6.")


    def test_party_time_2(self):
        self.assertEqual(('John', 'Lola', 'Chris'), hw.party_time([('John', 1), ('Mary', 7), ('Lola', 3), ('Rachel', 9), ('Chris', 3)], 3), msg="Failed party_time w/ [('John', 1), ('Mary', 7), ('Lola', 3), ('Rachel', 9), ('Chris', 3)] and 3.")


    def test_party_time_3(self):
        self.assertEqual(('Hans', 'Mark', 'Fred', 'Isabell'), hw.party_time([('Fred', 5), ('Mark', 2), ('Ben', 10), ('Isabell', 5), ('Hans', 1)], 4), msg="Failed party_time w/ [('Fred', 5), ('Mark', 2), ('Ben', 10), ('Isabell', 5), ('Hans', 1)] and 4.")


    def test_party_time_4(self):
        self.assertEqual(('Mars', 'Tom'), hw.party_time([('Ellen', 3), ('Hannah', 2), ('Mars', 1), ('Wilson', 9), ('Tom', 1)], 2), msg="Failed party_time w/ [('Ellen', 3), ('Hannah', 2), ('Mars', 1), ('Wilson', 9), ('Tom', 1)] and 2.")


    def test_party_time_5(self):
        self.assertEqual(('Henry', 'Lauren', 'Michael'), hw.party_time([('Lauren', 2), ('Michael', 2), ('David', 2), ('Henry', 1)], 3), msg="Failed party_time w/ [('Lauren', 2), ('Michael', 2), ('David', 2), ('Henry', 1)] and 3.")


    def test_ocd_1(self):
        self.assertEqual([(1, 1, 2), (2,), (3, 4, 8, 12)], hw.ocd([(1,2,3), (2,), (4,1,8,12)]), msg="Failed ocd w/ [(1,2,3), (2,), (4,1,8,12)].")


    def test_ocd_2(self):
        self.assertEqual([(1, 1, 2, 2), (2,), (3, 4, 7, 8)], hw.ocd([(4,3,8,1), (1,), (2,2,2,7)]), msg="Failed ocd w/ [(4,3,8,1), (1,), (2,2,2,7)].")


    def test_ocd_3(self):
        self.assertEqual([(0, 1, 1, 2), (3,), (4,)], hw.ocd([(4,3,2,1), (0,), (1,)]), msg="Failed ocd w/ [(4,3,2,1), (0,), (1,)].")


    def test_ocd_4(self):
        self.assertEqual([(1, 2, 3), (4, 4, 4), (5, 7, 8, 8, 23)], hw.ocd([(8,4,4), (23,5,7), (1,2,8,3,4)]), msg="Failed ocd w/ [(8,4,4), (23,5,7), (1,2,8,3,4)].")


    def test_ocd_5(self):
        self.assertEqual([(0, 1), (3, 4, 5), (6, 7, 7, 8, 9)], hw.ocd([(7,3), (1,9,0), (8,7,6,5,4)]), msg="Failed ocd w/ [(7,3), (1,9,0), (8,7,6,5,4)].")


if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW5")
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
