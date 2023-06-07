import pytest
from lib.present import Present

def test_present():
    present = Present()
    present.wrap("Bike")

#Testing wrap
# code below stores any error message as e
    with pytest.raises(Exception) as e:
        present.wrap("Car") #We need something that raises an error
    error_message = str(e.value)

    assert error_message == "A contents has already been wrapped."

# Testing unwrap
    new_present = Present()
    with pytest.raises(Exception) as e:
        new_present.unwrap()
    error_message = str(e.value)

    assert error_message == "No contents have been wrapped."
