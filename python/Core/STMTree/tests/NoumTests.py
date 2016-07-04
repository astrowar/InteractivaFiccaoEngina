import unittest

from SObjects import *
from SAssertions import SAssertion, SAssertionExecution


def new_assertion() -> SAssertion:
    return SAssertion()


class NoumTest(unittest.TestCase):
    def test_create(self):
        asst = SAssertionExecution()
        d = SDefineInstancia(SNoum("Book"), KdThing())
        self.assertEqual(asst.kind_of(SNoum("Book")), None)  # create but not execute
        asst.eval(d)
        nkind = asst.kind_of(SNoum("Book"))
        self.assertEqual(nkind, KdThing())  # after execution
        print("create")


class NoumTestProperty(unittest.TestCase):
    asst = new_assertion()

    def setUp(self):
        asst = SAssertionExecution()

    def test_create_1(self):
        asst = SAssertionExecution()
        d = SDefineKind(SNoum("Book"), KdThing())
        asst.eval(d)
        d = SDefinePropertyBinary(SNoum("Book"), SNoum("small"), SNoum("big"))
        asst.eval(d)
        ret = asst.query_is(SNoum("Book"), SNoum("small"))
        self.assertEqual(ret, None)

    def test_create_2(self):
        asst = SAssertionExecution()
        dkind = SDefineKind(SNoum("Book"), KdThing())
        dprop = SDefinePropertyBinary(SNoum("Book"), SNoum("small"))
        asst.eval(dkind)
        asst.eval(dprop)

    def test_create_3(self):
        asst = SAssertionExecution()
        dkind = SDefineKind(SNoum("Book"), KdThing())
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        dprop = SDefinePropertyEnumerate(SNoum("Book"), values)
        asst.eval(dkind)
        asst.eval(dprop)

    def test_create_4(self):
        asst = SAssertionExecution()
        dkind = SDefineKind(SNoum("Book"), KdThing())
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        dprop = SDefinePropertyEnumerate(SNoum("Book"), values).usually(SNoum("normal"))
        asst.eval(dkind)
        asst.eval(dprop)

    def test_create_5(self):
        asst = SAssertionExecution()
        dkind = SDefineKind(SNoum("Book"), KdThing())
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        dprop = SDefinePropertyEnumerate(SNoum("Book"), values).usually(SNoum("normal")).never(SNoum("big"))

        asst.eval(dkind)
        asst.eval(dprop)

    def test_create_6(self):
        asst = SAssertionExecution()
        dkind = SDefineKind(SNoum("Book"), KdThing())
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        dprop =  SDefinePropertyEnumerate(SNoum("Book"), values).usually(SNoum("normal"))
        print(list(asst.assertions.definitions(asst.kind_definition(SNoum("Book")))))
        asst.eval(dkind)
        asst.eval(dprop)
        with self.assertRaises(ValueError ):
            dprop =  SDefinePropertyEnumerate(SNoum("Book"), values).never(SNoum("big"))   # error
            asst.eval(dprop)