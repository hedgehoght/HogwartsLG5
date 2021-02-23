
def inc(x):
    return x + 1

def test_answer():
    print("这是我的第一条测试用例")
    assert inc(3) == 4

def test_foo():
    print("这是我的第二条测试用例")
    assert inc(2) == 3

def test_5():
    print("这是我的第三条测试用例")
    assert inc(5) == 6