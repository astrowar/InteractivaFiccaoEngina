from typing import List


class SAtom:
    def __init__(self):
        pass

    def eval(self, local_args, memm):
        raise Exception("abstract call")

    @property
    def items(self):
        return []


SNone = SAtom()


class SStack:
    def __init__(self):
        self.variables = {}
        self.local_arguments = []

    def push_arguments(self):
        pass

    def pop_arguments(self):
        pass

    def set_variable(self, name: str, value: SAtom):
        self.variables[name] = value

    def get_variable(self, name: str) -> object:
        return self.variables.get(name, None)


class SNoum:
    def __init__(self, _noum: str):
        self.noum = _noum

    def eval(self, local_args, memm):
        return self.noum

    def __repr__(self):
        return self.__class__.__name__ + ":" + self.noum

    def __eq__(self, other):
        if isinstance(other, SNoum):
            return self.noum == other.noum
        return False


class SNumber(SAtom):
    def __init__(self, _value: int) -> None:
        super().__init__()
        self.value = _value

    def eval(self, local_args, memm):
        return self.value

    def __repr__(self):
        return self.__class__.__name__ + ":" + str(self.value)

    def __eq__(self, other):
        if isinstance(other, SNumber):
            return self.value == other.value
        return False


class SArgument(SAtom):
    def __init__(self, i: int):
        super().__init__()
        self.argIndex = i

    def __repr__(self):
        return self.__class__.__name__ + ":" + str(self.argIndex)

    def __eq__(self, other):
        if isinstance(other, SArgument):
            return self.argIndex == other.argIndex
        return False

    def eval(self, local_args, memory):
        a1 = local_args[self.argIndex]
        # if isinstance(a1, SAtom):
        #     return a1.eval(local_args, memory)
        return a1


class SAdd(SAtom):
    def __init__(self, *args: [SAtom]):
        super().__init__()
        self.args = args

    @property
    def items(self):
        return self.args

    def eval(self, local_args, memory):
        a1 = self.args[0]
        a2 = self.args[1]
        if isinstance(a1, SAtom):
            a1 = self.args[0].eval(local_args, memory)
        if isinstance(a2, SAtom):
            a2 = self.args[1].eval(local_args, memory)

        return SNumber(a1 + a2)

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self.args) + "]"

    def __eq__(self, other):
        if isinstance(other, SAdd):
            r = [i for i, j in zip(self.items, other.items) if i != j]
            return r == []
        return False


const_types = [SNumber, SNoum]


class SVar(SAtom):
    def __init__(self, name, memm: SStack):
        super().__init__()
        self.name = name
        self.memm = memm

    @property
    def items(self):
        mref = self.memm.get_variable(self.name)
        return mref.items

    def eval(self, arguments, memm):
        return self.ref.eval(arguments, memm)

    def set_reference(self, aref: SAtom):
        self.memm.set_variable(self.name, aref)

    def set_value(self, aref: SAtom):
        if aref in const_types:
            self.memm.set_variable(self.name, aref)
        else:
            raise TypeError("only Const Types is alowed")

    def __repr__(self):
        mref = self.memm.get_variable(self.name)
        return self.__class__.__name__ + " " + self.name + "=" + mref.__repr__()

    def __eq__(self, other: SAtom):
        mref = self.memm.get_variable(self.name)
        return mref == other


class SFunc(SAtom):
    def __init__(self, body: List[SAtom]):
        super().__init__()
        self.body = body

    @property
    def items(self):
        return self.body

    def eval(self, arguments, memm):
        next_args = [aa.eval(arguments, memm) for aa in arguments]
        for b in self.body:
            yield b.eval(next_args, memm)


class SList(SAtom):
    def __init__(self, _items: [SAtom]):
        """

        :type _items: [SAtom]
        """
        super().__init__()
        self._items = _items

    @property
    def items(self):
        return self._items


# operador da lista .. retorna true se tudo for true
class SAll(SAtom):
    def __init__(self, _lista: SList, pred: SFunc):
        super().__init__()
        self.pred = pred
        self.lista = _lista

    def eval(self, local_args, memm):
        for item in self.lista.items:
            if not self.pred.eval([item], memm):
                return False
        return True


afunc = SFunc([SAdd(SArgument(0), SArgument(1))])  # f(x,y) =  x + y
# print(afunc.fcall([SNoum("a"), SNoum("b")]))

print(SArgument(0).eval([SNumber(1), SNumber(2)], None))
print(SArgument(1).eval([SNumber(1), SNumber(2)], None))

for k in afunc.eval([SNumber(1), SNumber(1)], {}):  # f(1,2)
    print(k)
