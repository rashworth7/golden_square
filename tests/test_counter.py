from lib.counter import Counter

def test_counter():
    counter = Counter()
    counter.add(4)
    
    result = counter.report()
    assert result == f"Counted to 4 so far."

    counter.add(3)
    new_result = counter.report()
    assert new_result == f"Counted to 7 so far."