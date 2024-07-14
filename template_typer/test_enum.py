from enum import Enum, StrEnum


class ConstantRegistry(StrEnum):
    ONE = "fezfezfezfez"


class NeuralNetwork(str, Enum):
    simple = "lol"
    conv = "conv"
    lstm = "lstm"


if __name__ == "__main__":
    print(NeuralNetwork.simple)
    print(ConstantRegistry.ONE)
