# Link: https://leetcode.com/problems/simple-bank-system/
#Q: 2043. Simple Bank System

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {}
        for index, value in enumerate(balance):
            self.balance[index + 1] = value
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if account1 in self.balance and account2 in self.balance:
            if self.balance[account1] >= money:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        
        if account in self.balance:
            self.balance[account] += money
            return True
        else:
            return False
            
    def withdraw(self, account: int, money: int) -> bool:
        
        if account in self.balance:
            if self.balance[account] >= money:
                self.balance[account] -= money
                return True
            else:
                return False
        else:
            return False
