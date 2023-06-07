from lib.report_length import report_length

def test_report_length():
    name = "Rich"
    name_len = len(name)
    assert report_length(name) == f"This string was {name_len} characters long."
