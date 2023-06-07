from lib.string_builder import StringBuilder

def test_string_builder():
    string_builder = StringBuilder()

    string_builder.add("Bradley")

    result = string_builder.output()
    length = string_builder.size()

    assert result == "Bradley"
    assert length == len("Bradley")

    string_builder.add("Rich")

    result = string_builder.output()
    length = string_builder.size()

    assert result == "BradleyRich"
    assert length == len("BradleyRich")