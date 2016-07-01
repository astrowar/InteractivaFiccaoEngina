import unittest

from STMTree import *


class MyTest(unittest.TestCase):
    def test_arg(self):
        x = (SArgument(0).eval([SNumber(1), SNumber(2)], None))
        self.assertEqual(x, SNumber(1))

    def test_arg_out(self):
        with self.assertRaises(IndexError):
            x = (SArgument(2).eval([SNumber(1), SNumber(2)], None))

    def test_arg_swap(self):
        fswap = lambda x: [SArgument(1).eval(x, None), SArgument(0).eval(x, None)]
        ret = fswap([SNoum("A"), SNoum("B")])
        self.assertEqual(ret, [SNoum("B"), SNoum("A")])

    def test_var1(self):
        mmem = SStack()
        v1 = SVar("X", mmem)
        self.assertEqual(v1, None)

    def test_var2(self):
        mmem = SStack()
        v1 = SVar("X", mmem)
        v1.set_reference(SNoum("B"))
        self.assertEqual(v1, SNoum("B"))

    def test_var3(self):
        mmem = SStack()
        v1 = SVar("X", mmem)
        v2 = SVar("Y", mmem)
        v2.set_reference(SNoum("B"))
        v1.set_reference(v2)
        self.assertEqual(v1, SNoum("B"))

    def test_var4(self):
        mmem = SStack()
        v1 = SVar("X", mmem)
        v2 = SVar("Y", mmem)
        v1.set_reference(v2)
        v2.set_reference(SNoum("B"))  # bind after ??
        self.assertEqual(v1, SNoum("B"))

    def test_var5(self):
        mmem = SStack()
        v1 = SVar("X", mmem)
        v2 = SVar("Y", mmem)
        v3 = SVar("Z", mmem)
        v4 = SVar("W", mmem)
        v2.set_reference(v1)
        v3.set_reference(v2)
        v4.set_reference(v3)  # 4  chains !!
        v1.set_reference(SNoum("A"))  # Bind to Value
        self.assertEqual(v4, SNoum("A"))
