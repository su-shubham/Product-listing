from app.basic_operations import add,subtract,divide,multiply
from app.basic_operations import BankAccount
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_amount():
    return BankAccount(50)

@pytest.mark.parametrize("x,y,z",[
(1,2,3),
(21,1,22),
(9,8,17)
])
def test_add(x,y,z):
    assert add(x,y)==z

def test_subtract():
    assert subtract(3,2)==1

def test_multiply():
    assert multiply(4,5)==20

def test_divide():
    assert divide(20,5)==4

def test_set_initial_amount(zero_bank_account):
    # bank_amount = BankAccount(50)
    assert zero_bank_account.balance == 0

def test_withdraw(bank_amount):
    bank_amount.withdraw_balance(20)
    assert bank_amount.balance==30 

def test_deposit(bank_amount):
    bank_amount.deposit_balance(20)
    assert bank_amount.balance==70

def test_bank_interest(bank_amount):
    bank_amount.interest()
    assert round(bank_amount.balance,5)==55

@pytest.mark.parametrize("x,y,z",[
    (70,20,50),
    (100,80,20),
    (1000,300,700)   
])
def test_bank_transcation(zero_bank_account,x,y,z):
    zero_bank_account.deposit_balance(x)
    zero_bank_account.withdraw_balance(y)
    assert zero_bank_account.balance == z 
    