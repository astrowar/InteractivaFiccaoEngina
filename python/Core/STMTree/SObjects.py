from STMTree import SStack, SAtom, SNoum


class SKind:
    def __init__(self, named: str, kind=None):
        """

        :type kind: SKind
        """

        self.name = named

        self.kind = kind

    def __eq__(self, other):
        if isinstance(other, SKind):
            return other.name == self.name
        return False




class KdThing(SKind):  # Kd => Kind
    def __init__(self):
        super().__init__("Thing")


class SCommand(SAtom):
    pass


class SDefineKind(SCommand):
    def __init__(self, noum: SNoum, kind: SKind = None):
        super().__init__()
        self.noum = noum
        self.kind = kind

        # def eval(self):
        #
        #     if kinds.get(self.noum.noum, None) is not None:
        #         raise KeyError("Kind altered exist ")
        #     kinds[self.noum.noum] = self.kind


class SDefineInstancia(SCommand):
    def __init__(self, noum: SNoum, kind:SKind):
        super().__init__()
        self.noum = noum
        self.kind = kind

        # def eval(self):
        #     instancias[self.noum.noum] = self.kind


def noum_negate(x: SNoum) -> SNoum:
    return SNoum("not " + x.noum)


class VConstraint(object):
    def __init__(self, noum: SNoum, w: float):
        self.value = noum
        self.weight = w


class SDefinePropertyBase(SCommand):
    def __init__(self, kind_noum: SNoum):

        super().__init__()
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

    @property
    def defined_keywords(self) -> [SNoum]:
        return []

    def has_collision(self, d) -> bool:
        for i in d.defined_keywords():
            for j in self.defined_keywords():
                if i == j:
                    return True

        return False

        # def eval(self):
        #     if not Assertion.is_kind(self.kind_noum):
        #         raise KeyError("This noum is not a kind")
        #
        #     bkind = Assertion.kind(self.kind_noum)
        #     for ds in bkind.defines:
        #         if self.has_collision(ds):
        #             raise Exception("definition noum alread exist")
        #
        #     bkind.define(self)
        #     pass


class SDefinePropertyUnary(SDefinePropertyBase):
    def __init__(self, kind_noum: SNoum, value: SNoum):
        super().__init__(kind_noum)
        self.value = value

    def eval(self):
        super(SDefinePropertyUnary, self).eval()
        pass

    def defined_keywords(self) -> [SNoum]:
        return self.value


class SDefinePropertyBinary(SDefinePropertyBase):
    def __init__(self, kind_noum: SNoum, value_true: SNoum, value_false=None):
        super().__init__(kind_noum)
        self.values = [value_true]
        if value_false is None:
            self.values.append(noum_negate(value_true))
        else:
            self.values.append(value_false)

    def eval(self):
        super(SDefinePropertyBinary, self).eval()
        pass

    def defined_keywords(self) -> [SNoum]:
        return self.values


class SDefinePropertyEnumerate(SDefinePropertyBase):
    def __init__(self, kind_noum: SNoum, values: [SNoum]):
        super().__init__(kind_noum)
        self.values = values

    def eval(self):
        super(SDefinePropertyEnumerate, self).eval()
        pass

    def defined_keywords(self) -> [SNoum]:
        return self.values
