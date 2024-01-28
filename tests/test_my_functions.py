import pytest
import source.my_function as my_function

def test_add():
    result = my_function.add(2,5)
    assert result == 7

# def test_add1():
#     result = my_function.add(2,5)
#     assert result == 9

def test_add_string():
    result = my_function.add("I like " , "Shinchan.")
    assert result == "I like Shinchan."

def test_sub():
    result = my_function.sub(4,2)
    assert result == 2

def test_div():
    with pytest.raises(ZeroDivisionError):
        result = my_function.divide(10,0)
    #assert True
