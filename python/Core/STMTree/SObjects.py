from STMTree import SStack, SAtom, SNoum

memoryPool = SStack()
definitions = {}
instancias = {}
kinds = {}


class SKind:
    def __init__(self, named: str):
        self.name = named
        self.defines = []
        kinds[self.name] = self

    def __eq__(self, other):
        if isinstance(other, SKind):
            return other.name == self.name
        return False

    def define(self, definition ):
        self.defines.append(definition)



class KdThing(SKind):  # Kd => Kind
    def __init__(self):
        super().__init__("Thing")


class Assertion:
    def __init__(self):
        pass

    @staticmethod
    def kind(noum: SNoum):
        by_instance = instancias.get(noum.noum, None);
        if by_instance is not None:
            return by_instance
        by_kind = kinds.get(noum.noum, None);
        return by_kind

    @staticmethod
    def is_kind(noum: SNoum):
        by_kind = kinds.get(noum.noum, None);
        return by_kind is not None

    @staticmethod
    def is_instance(noum: SNoum):
        by_instance = instancias.get(noum.noum, None);
        return by_instance is not None

    @staticmethod
    def clear( ):
        global definitions
        global instancias
        global kinds
        definitions = {}
        instancias = {}
        kinds = {}


class SDefineKind(SAtom):
    def __init__(self, noum: SNoum, kind:SKind = None ):
        super().__init__()
        self.noum = noum
        self.kind = kind

    def eval(self):
        global kinds
        if kinds.get(self.noum.noum, None) is not None:
            raise KeyError("Kind alweread exist ")
        kinds[self.noum.noum] = self.kind


class SDefine(SAtom):
    def __init__(self, noum: SNoum, kind):
        super().__init__()
        self.noum = noum
        self.kind = kind

    def eval(self):
        instancias[self.noum.noum] = self.kind


def noum_negate(x: SNoum) -> SNoum:
    return SNoum("not " + x.noum)


class VConstraint(object):
    def __init__(self, noum: SNoum, w: float):
        self.value = noum
        self.weight = w


class SDefinePropertyBase:
    def __init__(self, kind_noum: SNoum):

        self.kind_noum = kind_noum
        self.value_constraints = []

    def is_in_options(self, x):
        return True

    def usually(self, noum: SNoum):
        if not self.is_in_options(noum):
            raise KeyError("value is not in list of values allowed")
        self.value_constraints.append(VConstraint(noum, 1.0))
        return self

    def never(self, noum: SNoum):
        if not self.is_in_options(noum):
            raise KeyError("value is not in list of values allowed")
        self.value_constraints.append(VConstraint(noum, -10.0))
        return self

    def always(self, noum: SNoum):
        if not self.is_in_options(noum):
            raise KeyError("value is not in list of values allowed")
        self.value_constraints.append(VConstraint(noum, 10.0))
        return self

    def eval(self):
        if not Assertion.is_kind(self.kind_noum):
            raise KeyError("This noum is not a kind")

        #check for collision
        bkind = kinds.get(self.kind_noum.noum, None);

        bkind.define( self )
        pass


class SDefinePropertyUnary(SDefinePropertyBase):
    def __init__(self, kind_noum: SNoum, value):
        super().__init__(kind_noum)
        self.value = value

    def eval(self):
        super(SDefinePropertyUnary,self).eval()
        pass


class SDefinePropertyBinary(SDefinePropertyBase):
    def __init__(self, kind_noum: SNoum, value_true, value_false=None):
        super().__init__(kind_noum)
        self.values = [value_true]
        if value_false is None:
            self.values.append(noum_negate(value_true))
        else:
            self.values.append(value_false)

    def eval(self):
        super(SDefinePropertyBinary, self).eval()
        pass


class SDefinePropertyEnumerate(SDefinePropertyBase):
    def __init__(self, kind_noum: SNoum, values):
        super().__init__(kind_noum)
        self.values = values

    def eval(self):
        super(SDefinePropertyEnumerate, self).eval()
        pass
