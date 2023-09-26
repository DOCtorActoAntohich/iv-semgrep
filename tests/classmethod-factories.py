class SomeDude:
    def __init__(self, a: int, b: float, c: bool) -> None:
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def create_dude():
        # ruleid: classmethod-factories
        dude = SomeDude(1, 2, True)
        return dude

    @staticmethod
    def create_dude_again(a: int, b: float, c: bool) -> "SomeDude":
        # ruleid: classmethod-factories
        return SomeDude(a, b, c)

    @classmethod
    def create_dude_one_more_time(cls, a: int) -> "SomeDude":
        # ruleid: classmethod-factories
        boi = SomeDude(a, float(a), False)
        return boi

    @classmethod
    def create_dude_last_resort(cls, c: bool) -> "SomeDude":
        # ruleid: classmethod-factories
        return SomeDude(0, 0, c)

    @classmethod
    def create_dude_final_time(cls, a: int, b: float, c: bool) -> "SomeDude":
        # ok: classmethod-factories
        return cls(a, b, c)

    @classmethod
    def create_dude_final_time_for_real(cls, a: int, b: float, c: bool) -> "SomeDude":
        # ok: classmethod-factories
        dude_person_guy = cls(a, b, c)
        return dude_person_guy
