import pytest

def divide(first_num:float, second_num:float)->float:
    if(second_num == 0):
        return
    result = first_num/second_num
    return result

def test_happy_case():
    assert divide(10.0, 5.0) == 2
    
def test_divide_zero():
    assert divide(10, 0) == None