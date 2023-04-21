#  pytest file name should begin with test_
#  pytest test should be written in functions - it is standard, don't ask
#  test function also should begin with test_
import pytest

#  you can mark test and run all test with this mark name from console with -m name
#  to run pytest properly -> edit configurations -> + -> python test -> pytest

@pytest.mark.smoke
# @pytest.mark.skip  #  will skip test when running all tests
@pytest.mark.xfail  # will run the tst but will not report fail
def test_firstProgram():
    print("Bye")

def test_secondProgramCreditCard():
    print("Bad day to you")
