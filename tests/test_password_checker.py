import pytest
from lib.password_checker import PasswordChecker

def test_password_checker():
    password_1 = "test"
    password_2 = "this_is_a_strong_password"
    password_3 = "password"

    checker = PasswordChecker()

# Catches the exception error so it doesn't crash program. Stores as e_value
    with pytest.raises(Exception) as e:
        checker.check(password_1)
    e_value = str(e.value)

    assert e_value == "Invalid password, must be 8+ characters."
    assert checker.check(password_2) == True
    assert checker.check(password_3) == True

  
