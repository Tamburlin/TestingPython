import pytest

def test_fixture_demo(setup):
    print("lalala")


@pytest.mark.smoke
def test_stringCreditCard():
    x = "Bye"
    assert x == "Bye"
