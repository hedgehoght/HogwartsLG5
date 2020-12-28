import pytest
import yaml
from pytest_HT_1.calculator import Calculator

def open_file():
    with open("./data.yml") as f:
        data = yaml.safe_load(f)
        #print(data)
    return data

class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def setup(self):
        print("\n开始计算")
    def teardown(self):
        print("\n计算结束")

    @pytest.mark.parametrize("a,b,expect",open_file()["add"],ids=open_file()["myids"])
    # 加
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",open_file()["sub"],ids=open_file()["myids"])
    # 减
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",open_file()["mul"],ids=open_file()["myids"])
    # 乘
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",open_file()["div"],ids=open_file()["myids"])
    # 除
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
