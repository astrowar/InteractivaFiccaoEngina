from typing import List, Union


class SAtom:
    def __init__(self):
        pass

    def eval(self, local_args):
        """

        :type local_args: [SAtom]
        """
        raise Exception("abstract call")

    @property
    def items(self):
        return []


SNone = SAtom()


class SMemory:
    """ classe que organiza a memoria de variaveis """

    def __init__(self):
        self.buff = {}
        pass

    def __getitem__(self, item: str) -> SAtom:
        return self.buff[item]

    def __setitem__(self, key:  Union[str,'SVar'], value: SAtom) -> object:
        if isinstance(key, SVar):
            self.buff[key.name] = value
        else:
            self.buff[key] = value

    def get_variable(self, name: str):
        return self[name]

    def set_variable(self, name: str, aref: SAtom):
        self[name] = aref


class SMemoryContext(SMemory):
    def __init__(self, back_context: SMemory = None):
        super().__init__()
        self.prev = back_context

    def __getitem__(self, item: str) -> SAtom:
        if item in self.buff:
            return self.buff[item]
        if self.prev is not None:
            return self.prev[item]
        return None


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


class SContextEvaluation:
    def __init__(self, arguments: [SAtom], memory: SMemoryContext):
        self.arguments = arguments
        self.memory = memory

    def get_variable_value(self, item: str) -> SAtom:
        return self.memory.get_variable(item)

    def set_variable_value(self, item: str, value: SAtom):
        self.memory.set_variable(item, value)

    def get_argument(self, index: int) -> SAtom:
        return self.arguments[index]


class SValue(SAtom):
    def __init__(self):
        super().__init__()


class SNoum(SValue):
    def __init__(self, _noum: str):
        super().__init__()
        self.noum = _noum

    def eval(self, local_args):
        return self.noum

    def __repr__(self):
        return self.__class__.__name__ + ":" + self.noum

    def __eq__(self, other):
        if isinstance(other, SNoum):
            return self.noum == other.noum
        return False


class SNumber(SValue):
    def __init__(self, _value: int) -> None:
        super().__init__()
        self.value = _value

    def eval(self, local_args):
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

    def eval(self, local_args:SContextEvaluation):
        a1 = local_args.get_argument(self.argIndex)
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

    def eval(self, local_args):
        a1 = self.args[0]
        a2 = self.args[1]
        if isinstance(a1, SAtom):
            a1 = self.args[0].eval(local_args)
        if isinstance(a2, SAtom):
            a2 = self.args[1].eval(local_args)

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
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def items(self):
        return []

    def eval(self, arguments):
        mref = arguments.memory.get_variable(self.name)
        if isinstance(mref , SValue):
            return mref
        return mref.eval(arguments )


    #def set_reference(self, aref: SAtom):
    #    ctx.memory.set_variable(self.name, aref)

    # def set_value(self, aref: SAtom):
    #     if isinstance(aref, SValue):
    #         ctx.memory.set_variable(self.name, aref)
    #     else:
    #         raise TypeError("only Const Types is alowed")

    def __repr__(self):
        # mref = ctx.memory.get_variable(self.name)
        return self.__class__.__name__ + " " + self.name

    def __eq__(self, other: SAtom):
        if isinstance(other, SVar):
            return other.name == self.name
        raise Exception("unable to compare variable per se")


class SFunc(SAtom):
    def __init__(self, body: List[SAtom]):
        super().__init__()
        self.body = body

    @property
    def items(self):
        return self.body

    def eval(self, arguments):
        next_args = [aa.eval(arguments) for aa in arguments]
        for b in self.body:
            yield b.eval(next_args)


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

    def eval(self, local_args):
        for item in self.lista.items:
            if not self.pred.eval([item]):
                return False
        return True



