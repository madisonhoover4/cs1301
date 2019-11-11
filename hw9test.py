"""
Georgia Institute of Technology - CS1301
Basic unittest for student usage in bankaccount.py homework.
"""
import unittest
from bank_account import *

__author__  = "Rachel Golding"
__version__ = "0.1"
__email__   = "golding.rh@gmail.com"
__date__    = "Spring 2017"

class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Rachel Golding", 20, 1000)
        self.person_2 = Person("Ari Waugh", 23, 1000000)
        self.person_3 = Person("Margs Marghuerita", 16)
        self.person_4 = Person("Nico Roderiguez", 21)
        self.person_5 = Person("Daniel Barrundia", 17, 0)
        self.bank_account_1 = BankAccount(self.person_1, "Savings", 2000)
        self.bank_account_2 = BankAccount(self.person_2, "Checking")
        self.bank_account_3 = BankAccount(self.person_3, "Youth Savings", 5)
        self.bank_account_4 = BankAccount(self.person_4, "Savings", 2000)
        self.bank_account_5 = BankAccount(self.person_5, "Youth Checking")
        self.bank_account_6 = BankAccount(self.person_5, "Checking")
        # TODO add more test cases yourself

    ################
    #   Person     #
    ################

    def test_a1_init_name(self):
        self.assertEqual(self.person_1.name, "Rachel Golding",  msg = "A person should be initialized with a name.")

    def test_a2_init_name_2(self):
        self.assertEqual(self.person_3.name, "Margs Marghuerita",  msg = "A person should be initialized with a name.")

    def test_a3_init_age(self):
        self.assertEqual(self.person_1.age, 20,  msg = "A person should be initialized with an age.")

    def test_a4_init_wallet(self):
        self.assertEqual(self.person_1.wallet, 1000,  msg = "A person should be initialized with a wallet.")

    def test_a5_default_wallet(self):
        self.assertEqual(self.person_3.wallet, 0,  msg = "A person should be defaulted with a 0 for wallet if not given.")

    def test_a6_default_acct(self):
        self.assertEqual(self.person_1.account, None,  msg = "A person should be defaulted with no account.")

    def test_a7_start_account(self):
        self.person_1.startAccount("Savings", 2000)
        self.assertEqual(self.person_1.account, self.bank_account_1,  msg = "Person_1 (Rachel Golding) should have an account initialized: Savings with $2000")

    def test_a8_start_account_2(self):
        self.person_2.startAccount("Checking")
        self.assertEqual(self.person_2.account, self.bank_account_2,  msg = "Person_2 should have an account initialized: Checking with $0")

    def test_a9_start_youth_account(self):
        self.person_3.startAccount("Savings", 5)
        self.assertEqual(self.person_3.account, self.bank_account_3,  msg = "Person_3 should have a Youth account initialized: Youth Savings with $5")

    def test_b1_start_youth_account_2(self):
        self.person_5.startAccount("Checking", 0)
        self.assertEqual(self.person_5.account, self.bank_account_5,  msg = "Person_5 should have a Youth account initialized: Youth Checking with $0")

    def test_b2_birthday(self):
        self.assertEqual(self.person_1.age, 20,  msg = "Person_1 should be 20")
        self.person_1.birthday()
        self.assertEqual(self.person_1.age, 21,  msg = "Person_1 had a birthday and should be 21 now.")

    def test_b3_birthday_1(self):
        self.assertEqual(self.person_3.age, 16,  msg = "Person_3 should be 16 going on 17")
        self.person_3.startAccount("Savings", 5)
        self.person_3.birthday()
        self.assertEqual(self.person_3.age, 17,  msg = "Person_3 is 16 going on 17, but is still 16!")
        self.assertEqual(self.person_3.account, self.bank_account_3,  msg = "Person_3 should have a Youth account initialized: Youth Savings with $5")

    def test_b4_birthday_2(self):
        self.assertEqual(self.person_5.age, 17,  msg = "Person_5 should be 17 going on 18")
        self.person_5.startAccount("Checking")
        self.person_5.birthday()
        self.assertEqual(self.person_5.age, 18,  msg = "Person_5 is 17 going on 18, but is still 17!")
        self.assertEqual(self.person_5.account, self.bank_account_6,  msg = "Person_5 turned 18, their bank account should become a Checking Account from Youth Checking.")

    def test_b5_empty_wallet(self):
        self.person_2.account = self.bank_account_2
        self.person_2.emptyWallet()
        self.assertEqual(self.bank_account_2.balance, 1000000,  msg = "Empty Wallet should deposit all money into bank account's balance")
        self.assertEqual(self.person_2.wallet, 0,  msg = "Empty Wallet should empty Person's wallet")

    def test_b6_empty_wallet_2(self):
        self.person_1.account = self.bank_account_1
        self.person_1.emptyWallet()
        self.assertEqual(self.bank_account_1.balance, 3000,  msg = "Empty Wallet should deposit all money into bank account's balance")
        self.assertEqual(self.person_1.wallet, 0,  msg = "Empty Wallet should empty Person's wallet")

    def test_b7_empty_wallet_3(self):
        self.person_4.account = self.bank_account_4
        self.person_4.emptyWallet()
        self.assertEqual(self.bank_account_4.balance, 2000,  msg = "Empty Wallet should deposit all money into bank account's balance")
        self.assertEqual(self.person_4.wallet, 0,  msg = "Empty Wallet should empty Person's wallet")



    ################
    # Bank Account #
    ################

    ################
    #     Inits    #
    ################

    def test_c1_init_acct_holder(self):
        self.assertEqual(self.bank_account_1.acct_holder, self.person_1, msg = "Account Holder should be initialized.")

    def test_c2_init_balance(self):
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Balance should be initialized to 2000.")

    def test_c3_init_balance_1(self):
        self.assertEqual(self.bank_account_2.balance, 0, msg = "Balance should be initialized to 0 if not provided.")

    ################
    #    Deposit  #
    ################

    def test_d1_deposit(self):
        boolean = self.bank_account_1.deposit(1000)
        self.assertEqual(self.bank_account_1.balance, 3000, msg = "Deposit should increase balance")

    def test_d2_deposit_1(self):
        boolean = self.bank_account_1.deposit(-1000)
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Cannot deposit negative amount")

    def test_d3_deposit_true(self):
        boolean = self.bank_account_1.deposit(1000)
        self.assertEqual(boolean, True, msg = "Deposit should return True when successful")

    def test_d4_deposit__false(self):
        boolean = self.bank_account_1.deposit(-1000)
        self.assertEqual(boolean, False, msg = "Deposit should return False when not successful")


    def test_d5_deposit_2(self):
        boolean = self.bank_account_1.deposit(0)
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Depositing 0 should not change balance.")


    ################
    #   Withdraw   #
    ################

    def test_e1_withdraw(self):
        self.bank_account_1.withdraw(1000)
        self.assertEqual(self.bank_account_1.balance, 1000, msg = "Withdraw should decrease balance")

    def test_e2_withdraw_1(self):
        self.bank_account_1.withdraw(-1000)
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Cannot withdraw negative amount")



    def test_e3_withdraw_2(self):
        self.bank_account_1.withdraw(0)
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Withdrawing 0 should not change balance.")

    def test_e4_withdraw_3(self):
        self.bank_account_1.withdraw(3000)
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Cannot withdraw more than in account.")

    def test_e5_withdraw_true(self):
        boolean = self.bank_account_1.withdraw(1000)
        self.assertEqual(boolean, True, msg = "Withdraw should return True when successful")

    def test_e6_withdraw_false(self):
        boolean = self.bank_account_1.withdraw(3000)
        self.assertEqual(boolean, False, msg = "Withdraw should return False when not successful")

    def test_e7_withdraw_false2(self):
        boolean = self.bank_account_1.withdraw(-3000)
        self.assertEqual(boolean, False, msg = "Withdraw should return False when not successful")


    ################
    #    Transfer  #
    ################

    def test_f1_tranfer(self):
        self.bank_account_1.transfer(self.bank_account_2, 1000)
        self.assertEqual(self.bank_account_1.balance, 1000, msg = "Transfer should decrease bank account's balance.")
        self.assertEqual(self.bank_account_2.balance, 1000, msg = "Transfer should increase bank account's balance.")

    def test_f2_transfer_1(self):
        boolean = self.bank_account_2.transfer(self.bank_account_1, 1000)
        self.assertEqual(boolean, False ,msg = "Can't transfer without enough money in account.")
        self.assertEqual(self.bank_account_2.balance, 0, msg = "Transfer shouldn't decrease bank account's balance if there is not enough money")
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Transfer shouldn't increase bank account's balance if there is not enough money")


    def test_f3_transfer_true(self):
        boolean = self.bank_account_1.transfer(self.bank_account_2, 1000)
        self.assertEqual(boolean, True, msg = "Withdraw should return True when successful")

    def test_f4_transfer_false(self):
        boolean = self.bank_account_2.transfer(self.bank_account_1, 1000)
        self.assertEqual(boolean, False, msg = "Withdraw should return False when not successful")


    ################
    #   batchDep   #
    ################

    def test_g1_batch_deposit(self):
        self.bank_account_1.batchDeposit("file.txt")
        self.assertEqual(self.bank_account_1.balance, 2110, msg = "Batch Deposit should change bank account balance")

    def test_g2_batch_deposit_1(self):
        self.bank_account_1.batchDeposit("file2.txt")
        self.assertEqual(self.bank_account_1.balance, 2000, msg = "Batch Deposit should not change bank account balance if there are no numbers in file")

    def test_g3_batch_deposit_2(self):
        amt = self.bank_account_1.batchDeposit("file.txt")
        self.assertEqual(amt, True, msg = "Batch Deposit should return True if amount deposited.")

    def test_g3_batch_deposit_2_false(self):
        amt = self.bank_account_1.batchDeposit("file2.txt")
        self.assertEqual(amt, False, msg = "Batch Deposit should return False if amount not deposited.")

    ################
    #   gt/lt/eq   #
    ################

    def test_h1_gt(self):
        boolean = self.bank_account_1 > self.bank_account_2
        self.assertEqual(boolean, True, msg = "Greater than is incorrect.")

    def test_h2_gt_1(self):
        boolean = self.bank_account_2 > self.bank_account_1
        self.assertEqual(boolean, False, msg = "Greater than is incorrect.")

    def test_h3_lt(self):
        boolean = self.bank_account_2 < self.bank_account_1
        self.assertEqual(boolean, True, msg = "Less than is incorrect.")

    def test_h4_lt_1(self):
        boolean = self.bank_account_1 < self.bank_account_2
        self.assertEqual(boolean, False, msg = "Less than is incorrect.")


    ################
    #   charity    #
    ################

    def test_i1_charity(self):
        aList = [self.bank_account_2, self.bank_account_3, self.bank_account_4, self.bank_account_5, self.bank_account_6]
        self.bank_account_1.giveToCharity(aList, 999)
        bList = [aList[0].balance, aList[3].balance, aList[4].balance, self.bank_account_1.balance]
        self.assertEqual(bList, [333,333,333,(2000-999)] ,msg = "Give To charity should split the charity and take away from the donator.")

    def test_i2_charity_1(self):
        aList = [self.bank_account_2, self.bank_account_3, self.bank_account_4, self.bank_account_5, self.bank_account_6]
        self.bank_account_1.giveToCharity(aList, 9999)
        bList = [aList[0].balance, aList[3].balance, aList[4].balance, self.bank_account_1.balance]
        self.assertEqual(bList, [0,0,0,2000] ,msg = "Not enough money to Give To charity.")

    def test_i3_charity_2(self):
        num = self.bank_account_1.giveToCharity([], 999)
        self.assertEqual(num, False, msg = "Cannot give to charity if there are no charities.")

    def test_i4_charity_true(self):
        aList = [self.bank_account_2, self.bank_account_3, self.bank_account_4, self.bank_account_5, self.bank_account_6]
        boolean = self.bank_account_1.giveToCharity(aList, 999)
        bList = [aList[0].balance, aList[3].balance, aList[4].balance, self.bank_account_1.balance]
        self.assertEqual(boolean, True, msg = "Give to charity should return True if successful.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BankAccountTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
