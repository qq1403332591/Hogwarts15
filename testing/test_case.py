import pytest

from pythoncode.jiasuanqi import Jisuanqi
from decimal import *
import yaml


class TestCalc():

    def setup_class(self):
        self.calc = Jisuanqi()
        print("计算开始")

    @pytest.mark.parametrize("a,b,c", [
        [1, 2, 3], [1, 0.01, 1.01], [1, -1, 0], [0.01, 0.02, 0.03], [0.01, -1, -0.99], [-1, -2, -3]],
                             ids=['zheng_zheng', 'zheng_xiao', 'zheng_fu', 'xiao_xiao', 'xiao_fu', 'fu_fu'])
    # zheng_zheng：整数和整数
    # zheng_xiao：整数和小数
    # zheng_fu：整数和负数
    # xiao_xiao：整数和负数
    # xiao_fu：小数和负数
    # fu_fu：负数和负数
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        assert result == c

    getcontext().prec = 4  # #设置精度

    @pytest.mark.parametrize("a,b,c", [
        [Decimal(80), Decimal(150.04), Decimal('-70.04').quantize(Decimal('0.00'))], [1, 0.01, 0.99], [1, -1, 2],
        [0.01, 0.02, -0.01], [0.01, -1, 1.01], [-1, -2, 1]
    ])
    def test_jianfa(self, a, b, c):
        result = self.calc.sub(a, b)
        assert result == c

    @pytest.mark.parametrize("a,b,c", [
        [1, 2, 2], [1, 0.01, 0.01], [1, -1, -1], [0.01, 0.02, 0.0002], [0.01, -1, -0.01], [-1, -2, 2]])
    def test_chengfa(self, a, b, c):
        result = self.calc.chengfa(a, b)
        assert result == c

    @pytest.mark.parametrize("a,b,c", [
        [1, 2, 0.5], [1, 0.01, 100], [Decimal(3), Decimal(-3.1456265), Decimal('-0.9537')], [0.01, 0.02, 0.5],
        [0.01, -1, -0.01], [-1, -2, 0.5]
    ])
    def test_chufa(self, a, b, c):
        result = self.calc.chufa(a, b)
        assert result == c

    def test_chu_zero(self, a=1, b=0):
        result = self.calc.zerochu(a, b)
        assert result == '除以0无意义'

    def teardown_class(self):
        print("计算结束啦")
