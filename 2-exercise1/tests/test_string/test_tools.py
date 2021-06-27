from text.tools import upper_case, revers






def test_upper_case1():
    assert upper_case("python") == "PYTHON"



# why this will failed 
def test_upper_case2():
    assert upper_case("lion") == "LOIN"


def test_revers1():
    assert revers("lion") == "noil"

# why this test will failed
def test_revers2():
    assert revers("LION") == "noil"