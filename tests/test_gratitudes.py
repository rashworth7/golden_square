from lib.gratitudes import Gratitudes

def test_gratitudes():
    gratitudes = Gratitudes()

    gratitudes.add("Food")

    result = gratitudes.format()

    assert result == "Be grateful for: Food"

    gratitudes.add("TV")

    result = gratitudes.format()

    assert result == "Be grateful for: Food, TV"

