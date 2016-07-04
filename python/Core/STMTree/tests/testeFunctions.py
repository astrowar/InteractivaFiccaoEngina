import unittest

from STMTree import *


def new_context(args=None) -> SContextEvaluation:
    if args is None:
        args = []
    mem = SMemoryContext()
    return SContextEvaluation(args, mem)


class MyTest(unittest.TestCase):
    def test_arg(self):
        context = new_context([SNumber(1), SNumber(2)])

        x = (SArgument(0).eval(context))
        self.assertEqual(x, SNumber(1))

    def test_arg_out(self):
        context = new_context([SNumber(1), SNumber(2)])
        with self.assertRaises(IndexError):
            x = (SArgument(2).eval(context))

    def test_arg_swap(self):
        fswap = lambda x: [SArgument(1).eval(x), SArgument(0).eval(x)]
        context = new_context([SNoum("A"), SNoum("B")])
        ret = fswap(context)
        self.assertEqual(ret, [SNoum("B"), SNoum("A")])

    def test_var1(self):
        v1 = SVar("X")
        self.assertEqual(v1, SVar("X"))

    def test_var2(self):
        context = new_context()
        context.set_variable_value("X", SNoum("B"))
        v1 = SVar("X")
        value = v1.eval(context)
        self.assertEqual(value, SNoum("B"))

    def test_var3(self):
        context = new_context()

        v_x = SVar("X")
        v_y = SVar("Y")
        context.set_variable_value("Y", SNoum("B"))
        context.set_variable_value("X", v_y)
        value_x = v_x.eval(context)
        self.assertEqual(value_x, SNoum("B"))

    def test_var4(self):
        context = new_context()
        v_x = SVar("X")
        v_y = SVar("Y")

        context.set_variable_value("X", v_y)
        context.set_variable_value("Y", SNoum("B"))
        value_x = v_x.eval(context)
        self.assertEqual(value_x, SNoum("B"))

    def test_var5(self):
        v1 = SVar("X")
        v2 = SVar("Y")
        v3 = SVar("Z")
        v4 = SVar("W")
        context = new_context()
        context.set_variable_value(v4, v3)
        context.set_variable_value(v3, v2)
        context.set_variable_value(v2, v1)
        context.set_variable_value(v1, SNoum('A'))

        value_4 = v4.eval(context)
        self.assertEqual(value_4, SNoum("A"))
