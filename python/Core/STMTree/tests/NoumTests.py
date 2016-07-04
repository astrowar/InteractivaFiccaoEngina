import unittest

from SObjects import *


class NoumTest(unittest.TestCase):
    def test_create(self):
        d = SDefine(SNoum("Book"), KdThing())
        self.assertEqual(Assertion.kind(SNoum("Book")), None)  # create but not execute
        d.eval()
        self.assertEqual(Assertion.kind(SNoum("Book")), KdThing())  # create but not execute
        print("create")


class NoumTestProperty(unittest.TestCase):
    def setUp(self):
        Assertion.clear()

    def test_create_1(self):
        Assertion.clear()
        SDefineKind(SNoum("Book"), KdThing()).eval()
        SDefinePropertyBinary(SNoum("Book"), SNoum("small"), SNoum("big")).eval()

    def test_create_2(self):
        Assertion.clear()
        SDefineKind(SNoum("Book"), KdThing()).eval()
        SDefinePropertyBinary(SNoum("Book"), SNoum("small")).eval()

    def test_create_3(self):
        Assertion.clear()
        SDefineKind(SNoum("Book"), KdThing()).eval()
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        SDefinePropertyEnumerate(SNoum("Book"), values).eval()

    def test_create_4(self):
        Assertion.clear()
        SDefineKind(SNoum("Book"), KdThing()).eval()
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        SDefinePropertyEnumerate(SNoum("Book"), values).usually(SNoum("normal")).eval()

    def test_create_5(self):
        Assertion.clear()
        SDefineKind(SNoum("Book"), KdThing()).eval()
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        SDefinePropertyEnumerate(SNoum("Book"), values).usually(SNoum("normal")).never(SNoum("big")).eval()

    def test_create_6(self):
        Assertion.clear()
        SDefineKind(SNoum("Book"), KdThing()).eval()
        values = [SNoum("small"), SNoum("big"), SNoum("normal")]
        SDefinePropertyEnumerate(SNoum("Book"), values).usually(SNoum("normal")).eval()
        print(Assertion.definitions(Assertion.kind(SNoum("Book"))))
        with self.assertRaises(Exception):
            SDefinePropertyEnumerate(SNoum("Book"), values).never(SNoum("big")).eval()  # error
