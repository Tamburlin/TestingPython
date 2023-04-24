import pytest


@pytest.fixture()
def setup():
    print("Set up")  # will run before functions with fixture name in args
    yield
    print("will be executed last")


@pytest.fixture()
def dataLoad():
    print("user data is being created")
    return ["Joe", "Shmoe", "rahulshettyacademy.com"]

@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
