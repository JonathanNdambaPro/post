import typing as t


def function_with_fixed_type(some_sequence: t.Sequence[str]) -> str:
    return some_sequence[1]


def function_with_not_fixed_type(some_sequence: t.Sequence[t.Any]) -> str:
    return some_sequence[1]


def some_function_add(value_1: int | float, value_2: int | float) -> int | float:
    return value_1 + value_2


U = t.TypeVar("U")


def funce_typevar(some_sequence: t.Sequence[U]) -> U:
    return some_sequence[1]


def funce_typevar_second_version[T](some_sequence: t.Sequence[T]) -> T:
    return some_sequence[1]


U = t.TypeVar("U")


def some_function_add_type_var_simpler(value_1: U, value_2: U) -> U:
    return value_1 + value_2


def some_function_add_type_var_compact[G](value_1: G, value_2: G) -> G:
    return value_1 + value_2


type FunctionBluePrintStr = t.Callable[[str, str], str]


def some_function(value_1: str, value_2: str) -> str:
    return value_1 + value_2


def some_function_bis(value_1: str, value_2: str) -> list[str]:
    return [value_1, value_2]


dict_value: FunctionBluePrintStr = {
    "some_key": some_function,
    "some_key_bis": some_function_bis,
}


class SomeClass[T]:
    def __init__(self, some_value_generic: T, some_value_generic_bis: T) -> None:
        self.some_value_generic = some_value_generic
        self.some_value_generic_bis = some_value_generic_bis

    def get_value(self) -> tuple[T, T]:
        return self.some_value_generic + self.some_value_generic_bis


class SomeClassRetuenItSelf:
    def return_self(self) -> t.Self:
        return self


class SomeClassReturnInstance:
    def return_instance(self) -> "SomeClassReturnInstance":
        return SomeClassReturnInstance()


type Mode = t.Literal["r", "rb", "w", "wb"]


def open_helper(file: str, mode: Mode) -> str: ...


def function_with_unpack_parameter[T](**kwargs: t.Unpack[T]) -> t.Any: ...


@t.runtime_checkable
class Closable(t.Protocol):
    def close(self): ...


class SomeClassChekable:
    def close(self):
        print("lol")


isinstance(Closable, SomeClassChekable)
