import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo1(self):
        print("lalala1")

    def test_fixture_demo2(self):
        print("lalala2")

    def test_fixture_demo3(self):
        print("lalala3")
