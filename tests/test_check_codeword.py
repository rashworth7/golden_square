from lib.check_codeword import check_codeword 

def test_check_codeword():
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("pig") == "WRONG!"
    assert check_codeword("home") == "Close, but nope."
