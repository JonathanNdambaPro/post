import re
import typing as t
import unicodedata
from functools import reduce


def pipe(*functions: t.Callable) -> t.Callable:
    return lambda x: reduce(lambda previous, next_: next_(previous), functions, x)


def normalise_string(element: str) -> str:
    cleaned_element = pipe(
        str.lower,
        lambda x: unicodedata.normalize("NFKD", x)
        .encode("ASCII", "ignore")
        .decode("ASCII"),
        lambda x: re.sub(r"[^\w\s-]", "", x),
        lambda x: re.sub(r"[-\s]+", "_", x),
        lambda x: x.replace("_and_", "_et_"),
        lambda x: x.strip("_"),
    )(element)
    return cleaned_element


words = [
    "Nom_utilisateur!@#$",
    "E-ma!l/Adresse^&*",
    "Télé#phoné%+",
    "Adréssè(domicile)!",
    "Âgè&",
    "Tëst%&^Str!ng",
    "Dàtâ_Cleansing@!",
    "Nor#malîzation++",
    "Py&thon_3.9",
    "Dév&ëlôpmen+t",
]

normalized_words = [normalise_string(word) for word in words]

if __name__ == "__main__":
    for original, normalized in zip(words, normalized_words):
        print(f"Original: {original}\nNormalisé: {normalized}\n")
