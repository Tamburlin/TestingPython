import pytest


@pytest.fixture()
def setup():
    print("Set up")  # will run before functions with fixture name in args
    yield
    print("will be executed last")

def test_fixture_demo(setup):
    print("lalala")


@pytest.mark.smoke
def test_stringCreditCard():
    x = "Bye"
    assert x == "Bye"
