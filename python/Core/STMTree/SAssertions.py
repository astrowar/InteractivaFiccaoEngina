from SObjects import SDefineKind, SDefineInstancia, SDefinePropertyEnumerate
from SObjects import SDefinePropertyBase, SCommand
from SObjects import SNoum, SKind


class SAssertion:
    def __init__(self):
        self.definitions_list = []  # [SDefinePropertyBase]
        self.kinds = {}  # [kindname_str -> SDefinekind]

        self.instancias = {}  # objetos

    def up_kind(self,
                noum: SNoum) -> SKind:
        by_instance = self.instancias.get(noum.noum, None)
        if by_instance is not None:
            return by_instance
        by_kind = self.kinds.get(noum.noum, None)
        return by_kind

    def is_kind(self, noum: SNoum) -> True:
        by_kind = self.kinds.get(noum.noum, None)
        return by_kind is not None

    def is_instance(self, noum: SNoum) -> bool:
        by_instance = self.instancias.get(noum.noum, None)
        return by_instance is not None

    def clear(self):

        self.definitions_list = []

        self.instancias = {}
        self.kinds = {}

    def definitions(self, kind_name: str) -> list:
        for v in self.definitions_list:
            if v.kind_noum.noum == kind_name:
                yield v

    def contains_noum_in_definitions(self, kind: SKind, n: SNoum):
        for d in self.definitions(kind.name):
            if n.noum in d.defined_keywords():
                return True
        return False


class SAssertionExecution:
    def __init__(self):
        self.assertions = SAssertion()

    def eval(self, data: SCommand):

        if isinstance(data, SDefineKind):
            return self.eval_SDefineKind(data)
        if isinstance(data, SDefineInstancia):
            return self.eval_SDefineInstancia(data)
        if isinstance(data, SDefinePropertyEnumerate):
            return self.eval_SDefinePropertyEnumerate(data)
        if isinstance(data, SDefinePropertyBase):
            return self.eval_SDefinePropertyBase(data)

    def eval_SDefineKind(self, data: SDefineKind):
        if self.assertions.kinds.get(data.noum.noum, None) is not None:
            raise KeyError("Kind altered exist ")
        self.assertions.kinds[data.noum.noum] = data.kind

    def eval_SDefineInstancia(self, data: SDefineInstancia):
        self.assertions.instancias[data.noum.noum] = data.kind

    def eval_SDefinePropertyBase(self, data: SDefinePropertyBase):
        if not self.assertions.is_kind(data.kind_noum):
            raise KeyError("This noum is not a kind")

        bkind = self.kind_definition(data.kind_noum)
        if bkind is None:
            raise Exception("kind does not exist ")
        for ds in self.assertions.definitions(data.kind_noum.noum):
            if data.has_collision(ds):
                print("???")
                raise ValueError("definition noum alread exist")

        self.assertions.definitions_list.append(data)

    def kind_definition(self, noum: SNoum) -> SKind:
        r = self.assertions.kinds.get(noum.noum, None)
        if r is None:
            return None
        return SKind(noum.noum, r.kind)

    def kind_of(self, noum: SNoum):
        r = self.assertions.kinds.get(noum.noum, None)
        if r is not None:
            return r.kind
        r = self.assertions.instancias.get(noum.noum, None)
        if r is not None:
            return r
        return None

    def query_is(self, noum: SNoum, param: SNoum):
        # Existe uma instancia com esse nome ?
        if self.assertions.is_instance(noum):
            raise NotImplementedError("Sorry...")
        # Existe um Kind ou instancia com esse nome ?
        if self.assertions.is_kind(noum):
            by_kind = self.assertions.kinds[noum.noum]
            if by_kind is not None:
                if self.assertions.contains_noum_in_definitions(by_kind, param):
                    return True

    def eval_SDefinePropertyEnumerate(self, data: SDefinePropertyEnumerate):
        self.eval_SDefinePropertyBase(data)
