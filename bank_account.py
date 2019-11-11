#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW9 - OOP - due Monday, Apr. 17, 2017
"""
__author__ = "YOUR NAME HERE"
__collaboration__ = """ YOUR COLLABORATION STATEMENT HERE """

import urllib.request

class BankAccount(object):

    def __init__(self, acct_holder, acct_type, balance = 0):
        """
        Write a constructor for a bank account below.
        The following attributes:
        acct_holder will be a Person object
        acct_type is a string
        balance should be defaulted to 0 if not provided to the constructor, is an int
        """
        self.acct_holder = acct_holder
        self.acct_type = acct_type
        self.balance = balance

    """
    Change Account Type should update Account Type to newType
    """

    def changeAccountType(self, newType):
        self.acct_type = newType
        
    """
    Deposit should update the balance of the bank account depending on amounnt:
    Returns True if deposits,
    False if amount is negative.

    """
    def deposit(self, amt):
        if amt < 0:
            return False
        else:
            self.balance += amt
            return True

    """
    Withdraw should update the balance of the bank account depending on amount:
    Returns True if withdraws,
    False if amount is negative or there is not enough in the account to withdraw.

    """
    def withdraw(self, amt):
        if amt > self.balance or amt < 0:
            return False
        
        else:
            self.balance -= amt
            return True

    """
    Batch Deposit should update the balance of the bank account depending on amounnt:
    Read the file and take all numbers that are alone on a line for deposit.
    Returns True if deposits,
    False if there is no amount.
    """
    def batchDeposit(self, file):
        with open(str(file), "r") as a:
            lines = a.readlines()
            total = 0
            current = self.balance
            for line in lines:
                try:
                   a= float(line)
                   self.balance += a
                except:
                    pass
            round(self.balance, 2)
        if self.balance == current:
            return False
        else:
            return True
        

    """
    Transfer should update the balance of both of the bank accounts depending on amounnt:
    Returns True if deposits,
    False if amount is negative or there is not enough in the account to withdraw from self.
    """
    def transfer(self, other, amt):
        if amt >= 0 and self.balance >= amt:
            other.balance += amt
            self.balance -= amt
            return True
        else:
            return False
            

    """
    Greater than compares balances of bank accounts
    Returns True if self is greater,
    False otherwise
    """
    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        else:
            return False
    


    """
    Less than compares balances of bank accounts
    Returns True if self is less,
    False otherwise
    """
    def __lt__(self, other):
        if self.balance < other.balance:
            return True
        else:
            return False
        
    """
    Returns True if all attributes are equal, otherwise False
    """
    def __eq__(self, other):
        if self.balance == other.balance and self.acct_type == other.acct_type and self.acct_holder == other.acct_holder:
            return True
        
        return False



    """
    Give to charity takes in a list of charities:
    list_charities: BankAccount Objects
    amount: int to donate

    Give the amount to the charities with the smallest balance.
    Split the amount if there is more than 1.

    Update the balances of both the account donating, and the
    charities receiving the donation.

    Return False if there are no charities in the list.
    """
    def giveToCharity(self, list_charities, amount):
        if len(list_charities) == 0:
            return False
        if self.balance < amount or amount < 0:
            return False
        
        newestlow = list_charities[0]
        smalllist = []
        smalllist.append(list_charities[0])
        for charity in list_charities:
            print("Charity 1", newestlow.balance, "Charity 2", charity.balance)
            if charity.__eq__(newestlow):
                continue
            elif charity.__lt__(newestlow):
                print("less than")
                newestlow = charity
                smalllist = []
                smalllist.append(charity)
                
            elif charity.balance == newestlow.balance:
                print("equal balance")
                smalllist.append(charity)
        amount = amount / len(smalllist)
        
        
        for charity in smalllist:
            print(charity.balance)
            self.transfer(charity, amount)
        return True
            

      
class Person(object):


    """
    Initialize name, age, and wallet
    Initialize account to None
    """
    def __init__(self, name, age, wallet = 0):
        self.name = str(name)
        self.age = int(age)
        self.wallet = int(wallet)
        self.account = None
        


    """
    Start a bank account based on the age of the Person:
    If the age is under 18, add "Youth" to the account type.
    eg: "Youth Savings" if a_type is "Savings"

    Default balance to 0 unless given.

    Update account attribute to this account.
    Note: a Person will have up to one account at any time.
    """
    def startAccount(self, a_type, balance = 0):
        if self.age >= 18:
            self.account = BankAccount(self, str(a_type), balance)
            
        else:
            self.account = BankAccount(self, "Youth " + str(a_type), balance)
        


    """
    Update age of Person by 1
    If the age is becomes 18, take away "Youth" from the account type (if there is an account)
    eg: "Savings" if a_type was "Youth Savings"
    """
    def birthday(self):
        self.age += 1
        if self.age == 18:
            if self.account.acct_type == "Youth Savings":
                self.account.changeAccountType("Savings")
            elif self.account.acct_type == "Youth Checking":
                self.account.changeAccountType("Checking")
            

    """
    Empty the wallet of the user into the bank account (if exists)
    Update wallet and account balance if applicable
    """
    def emptyWallet(self):
        if self.wallet > 0:
            self.account.balance += self.wallet
            self.wallet = 0
            return None
        return None
